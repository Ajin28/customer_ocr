from rest_framework import serializers
from common.enums.generic_enums import Gender

class Register_Request(serializers.Serializer):
    firstname = serializers.CharField()
    password = serializers.CharField()
    lastname = serializers.CharField()
    country = serializers.CharField()
    gender = serializers.CharField(max_length=10)
    created_by = serializers.CharField()

    def validate_gender(self, value):
        print(Gender.choices)
        if value in [Gender.choices]:
            return value
        else: 
            raise serializers.ValidationError("Please select a valid value fpr gender")
