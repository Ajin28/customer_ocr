from common.mixins import OCR_APIView, AWS_Mixin
from rest_framework.response import Response
from common.serializers import Upload_Document_Request
from common.models import CustomerDocument
from common.decorators import is_authenticated
from django.utils.decorators import method_decorator
from common.enums.env_enums import AWS_STORAGE_BUCKET_NAME


class UploadDocumentView(OCR_APIView, AWS_Mixin):
    
    # @method_decorator(is_authenticated)
    def post(self, request):
        req_data = self.validate_serializer(Upload_Document_Request, request.data)
        payload = list()
        if req_data["front_image"]:
            payload.append(self.upload_image_to_s3(req_data["front_image"]))
        if req_data["back_image"]:
            payload.append(self.upload_image_to_s3(req_data["back_image"]))
        return Response({
            "status": 1,
            "data": {"payload": {"files": payload, "country_id": req_data["country_id"], "document_set_id": req_data["document_set_id"]}, "links": [f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file_name}" for file_name in payload]}
        })


        
    
