from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            password = validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['nickname', 'email', 'password']

class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'