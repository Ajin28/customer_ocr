from rest_framework import serializers

class Extract_Data_Request(serializers.Serializer):
    files = serializers.ListField(child = serializers.CharField(), allow_empty= True, max_length = 2)
    document_set_id = serializers.CharField()
    country_id = serializers.CharField()
   

