from rest_framework import serializers

class Create_Customer_Request(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    country_id = serializers.CharField()
    gender = serializers.CharField()
    age = serializers.CharField(required = False)


