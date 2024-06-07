from rest_framework import serializers

class Login_Request(serializers.Serializer):
    firstname = serializers.CharField()
    password = serializers.CharField()
   
   