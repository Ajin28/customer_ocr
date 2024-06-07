from common.mixins import OCR_APIView, AWS_Mixin
from rest_framework.response import Response
from common.serializers import Create_Customer_Request
from common.models import Customer, CustomerDocument, DocumentSet, Country
from common.decorators import is_authenticated
from django.utils.decorators import method_decorator
from common.exceptions.rest_api_exception import RestAPIException

class CreateCustomerView(OCR_APIView, AWS_Mixin):
    
    @method_decorator(is_authenticated)
    def post(self, request):
        req_data = self.validate_serializer(Create_Customer_Request, request.data)
        req_data["created_by"] = request.user
        
        customer = {
            "created_by":request.user,
            "firstname": req_data["firstname"],
            "lastname": req_data["lastname"],
            "gender": req_data["gender"],
            "country_id": req_data["country_id"],
            "age": req_data["age"],
        }
        obj = Customer.objects.create(**customer)
        obj.save()
        customer_document = {
            "extracted_json" : req_data["extracted_data"],
            "front_image": req_data["front_image"],
            "back_image": req_data["back_image"],
            "customer_id": obj.id,
            "document_id": req_data["document_set_id"]
        }
        obj = CustomerDocument.objects.create(**customer_document)
        obj.save()

        return Response({
            "status": 1,
            "data": {
                "id": obj.id,    
            }
        })


        
    
