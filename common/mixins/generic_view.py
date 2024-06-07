"""
This module consists of Base API view to be used for class based requests to review manager
"""
from rest_framework import status
from rest_framework.views import APIView
from common.exceptions.rest_api_exception import RestAPIException


class OCR_APIView(APIView):
    ''' A generic APIView for reviews project '''

    def validate_serializer(self, serializer, req_data):
        ''' Validate serializer against request data '''
        req = serializer(data=req_data)
        if not req.is_valid():
            raise RestAPIException(f"Please provide a valid request data, {req.errors}")
        return req.validated_data

    
    def validate_many_serializer(self, serializer, req_data):
        ''' Validate serializer against request data '''
        req = serializer(data=req_data, many=True)
        if not req.is_valid():
            raise RestAPIException(f"Please provide a valid request data, {req.errors}")
        return req.validated_data

