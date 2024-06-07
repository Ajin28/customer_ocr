from common.mixins import OCR_APIView
from rest_framework.response import Response

class APIRoot(OCR_APIView):

    def get(self, request):
        base_url = request.build_absolute_uri('/')
        return Response({
            "urls":  [
                base_url+"admin/",
            ]
        })