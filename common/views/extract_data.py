from common.mixins import OCR_APIView, AWS_Mixin
from rest_framework.response import Response
from common.serializers import Extract_Data_Request
from common.models import DocumentSet, Country
from common.decorators import is_authenticated
from django.utils.decorators import method_decorator
from common.exceptions.rest_api_exception import RestAPIException

class ExtractDataView(OCR_APIView, AWS_Mixin):
    
    # @method_decorator(is_authenticated)
    def post(self, request):
        req_data = self.validate_serializer(Extract_Data_Request, request.data)
        extracted_data = dict()
        try:
            doc_type = DocumentSet.objects.get(id = req_data["document_set_id"])
        except DocumentSet.DoesNotExist:
            raise RestAPIException("Invalid Document Set Id")
        
        try:
            country = Country.objects.get(id = req_data["country_id"])
        except Country.DoesNotExist:
            raise RestAPIException("Invalid Document Set Id")

        if req_data["files"]:
            extracted_data = self.extract_text_from_document(req_data["files"])
        
        parsed_customer_data = dict()

        labels = doc_type.ocr_labels
        for field in labels:
            keys = labels[field] #firstname
            for ext_key in extracted_data:
                subkey_ext_keys = ext_key.split(" ")
                for subkeys in subkey_ext_keys:
                    if subkeys.lower() in keys:
                        parsed_customer_data[field] = extracted_data[ext_key].lower()

        return Response({
            "status": 1,
            "data": {
                "extracted_data": extracted_data,
                "document_set_id": doc_type.id,
                'country_id': country.id,
                "ocr_labels": labels,
                "parsed_customer_date": parsed_customer_data
            }
        })
                
        


        
    
