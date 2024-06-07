from common.mixins import OCR_APIView, AWS_Mixin
from rest_framework.response import Response
from common.serializers import Create_Customer_Request
from common.models import Customer
from common.decorators import is_authenticated
from django.utils.decorators import method_decorator

class CreateCustomerView(OCR_APIView, AWS_Mixin):
    
    @method_decorator(is_authenticated)
    def post(self, request):
        req_data = self.validate_serializer(Create_Customer_Request, request.data)
        req_data["created_by"] = request.user
        obj = Customer.objects.create(**req_data)
        obj.save()
        return Response({
            "status": 1,
            "data": {
                "id": obj.id,    
            }
        })


        
    
