from common.models import Customer, CustomUser, DocumentSet, CustomerDocument
from common.mixins import OCR_APIView, AWS_Mixin
from rest_framework.response import Response
from common.serializers import Create_Customer_Request
from common.models import CustomerDocument
from common.decorators import is_authenticated
from django.utils.decorators import method_decorator

class CustomerListView(OCR_APIView):

    @method_decorator(is_authenticated)
    def get(self, request):
        user_id = request.user.id
        response = list()
        queryset = Customer.objects.filter(created_by = user_id)

        for customer in queryset:
            documents = list()
            queryset = CustomerDocument.objects.filter(customer=customer.id).select_related('document')
            for document in queryset:
                documents.append({
                    "id": document.id,
                    "document_name": document.document.name,
                    "document_description": document.document.description,
                    "has_backside": document.document.has_backside,
                    "possible_data": document.document.ocr_labels,
                    "front_image":document.front_image,
                    "back_image": document.back_image,
                    "extracted_json": document.extracted_json
                })
            response.append({
                "id" : customer.id,
                "country" : customer.country.name,
                "firstname": customer.firstname,
                "lastname": customer.lastname,
                "gender": customer.gender,
                "age": customer.age,
                "documents": documents
            })

        return Response({
            "status": 1,
            "data": response
        })