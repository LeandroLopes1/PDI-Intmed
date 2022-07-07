from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario

    def validate_password(self, password):
        if len(password) < 6 or len(password) > 8:
            raise serializers.ValidationError('A senha deve ter entre 6 e 8 caracteres')
        return password
 
    def validate_email(self, email):
        if Usuario.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email já cadastrado')
        return email
      