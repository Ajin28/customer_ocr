import boto3
from common.enums.env_enums import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from trp import Document
from common.exceptions.rest_api_exception import RestAPIException
import os
import uuid
from datetime import datetime

class AWS_Mixin():
       
    def extract_text_from_id(self, document_name_list):
        
        textract = boto3.client('textract', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_S3_REGION_NAME)
        response = textract.analyze_id(
            DocumentPages= [
                {
                    'S3Object': {
                        'Bucket': AWS_STORAGE_BUCKET_NAME,
                        'Name': document_name
                    }
                }
            ],
        )
        # response = textract.analyze_document(
        #     DocumentPages=[
        #         {'Bytes': idcard_bytes},
        #     ]
        # )
        # print(response)
        
        # doc = Document(response)
        # extracted_dict = dict()
        # for page in doc.pages:
        #     for field in page.form.fields:
        #         extracted_dict[str(field.key)] = str(field.value)
                

        return response      
    

    def extract_text_from_document(self, document_name_list):

        textract = boto3.client('textract', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_S3_REGION_NAME)
        extracted_dict = dict()
        for document_name in document_name_list:
            response = textract.analyze_document(
                Document = {  
                    'S3Object': {
                        'Bucket': AWS_STORAGE_BUCKET_NAME,
                        'Name': document_name
                    },
              
                },
                FeatureTypes = ['FORMS']
            )
            doc = Document(response)
            for page in doc.pages:
                for field in page.form.fields:
                    extracted_dict[str(field.key)] = str(field.value)     

        return extracted_dict      
    
    def upload_image_to_s3(self, file):
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name=AWS_S3_REGION_NAME)

        try:
            file_name = self.generate_unique_filename(file.name)
            s3.upload_fileobj(file, AWS_STORAGE_BUCKET_NAME, file_name)
            return file_name
        except Exception as e:
            raise RestAPIException("Something went wrong while uploading image")
        
    def generate_unique_filename(self, original_filename):
        # Extract the file extension
        file_extension = os.path.splitext(original_filename)[1]
        # Generate a unique identifier
        unique_id = uuid.uuid4()
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        # Combine elements to create a unique filename
        unique_filename = f"{timestamp}_{unique_id}{file_extension}"
        return unique_filename