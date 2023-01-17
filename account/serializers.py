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
        #field = '__all__'
        #이것만 직렬화 하겠음
        fields = ['nickname', 'email', 'password']

class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #모두 직렬화하겠음
        fields = '__all__'