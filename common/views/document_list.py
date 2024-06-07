from common.models import Customer, CustomUser, DocumentSet, CustomerDocument
from common.mixins import OCR_APIView, AWS_Mixin
from rest_framework.response import Response
from common.serializers import Create_Customer_Request
from common.models import CustomerDocument
from common.decorators import is_authenticated
from django.utils.decorators import method_decorator

class DocumentListView(OCR_APIView):

    @method_decorator(is_authenticated)
    def get(self, request):
        response = list()
        queryset = DocumentSet.objects.filter(country__id = request.user.country_id)

       
        for document in queryset:
            response.append({    
                "document_name": document.name,
                "document_description": document.description,
                "has_backside": document.has_backside,
                "ocr_labels": document.ocr_labels,          
            })
            

        return Response({
            "status": 1,
            "data": response
        })