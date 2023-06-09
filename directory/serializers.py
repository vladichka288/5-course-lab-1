from rest_framework import serializers


class PhoneSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    phone_number1 = serializers.CharField(max_length=50)
    phone_number2 = serializers.CharField(max_length=50, required=False)
