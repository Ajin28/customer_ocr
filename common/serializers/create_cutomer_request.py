from rest_framework import serializers

class Create_Customer_Request(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    country_id = serializers.CharField()
    gender = serializers.CharField()
    age = serializers.CharField(default = None)
    extracted_data = serializers.DictField()
    front_image = serializers.CharField(default = None)
    back_image = serializers.CharField(default = None)
    document_set_id = serializers.CharField()
    files = serializers.ListField(child = serializers.CharField(), allow_empty= True, max_length = 2, default = [])



