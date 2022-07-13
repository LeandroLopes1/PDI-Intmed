from rest_framework import serializers


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField()

    class Meta:
        fields = ('email', 'password')
