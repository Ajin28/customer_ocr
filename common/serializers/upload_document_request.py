from rest_framework import serializers

class Upload_Document_Request(serializers.Serializer):
    front_image = serializers.FileField(default = None)
    back_image = serializers.FileField(default = None)
    document_set_id = serializers.CharField()
    country_id = serializers.CharField()

