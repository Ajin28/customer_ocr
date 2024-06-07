from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from functools import wraps
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.exceptions import APIException
from common.exceptions.rest_api_exception import RestAPIException
import jwt
from common.enums.env_enums import SECRET_KEY
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

def is_authenticated(*args, **kwargs):
    
    def wrap(request, *inner_args, **inner_kwargs):
        jwt_authenticator = JWTAuthentication()
        try:
            # Authenticate the request using JWT
            user, validated_token = jwt_authenticator.authenticate(request)
            # Attach the user to the request object
            request.user = user
        except Exception:
            return Response({"detail": "Authentication failed."}, status=status.HTTP_401_UNAUTHORIZED)
        
        return args[0](request, *inner_args, **inner_kwargs)
    return wrap


