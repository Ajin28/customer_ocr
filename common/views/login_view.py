from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from common.mixins import OCR_APIView
from rest_framework.response import Response
from common.models import CustomUser
from common.serializers import Login_Request
from django.contrib.auth import authenticate


class LoginView(OCR_APIView):
    
    def post(self, request, *args, **kwargs):

        req_data = self.validate_serializer(Login_Request, request.data)
        username = req_data.get("firstname")
        password = req_data.get("password")

        user = CustomUser.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            return Response({"error": "Invalid credentials"}, status=400)

    
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
