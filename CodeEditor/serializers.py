from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()
from django.conf import settings
from rest_framework.authtoken.models import Token
from editor_api.models import Code
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

        def create(self, validated_data):
            user = settings.AUTH_USER_MODEL.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = "__all__"
