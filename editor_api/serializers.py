from rest_framework import serializers
from .models import Code , Passed , Problem
from django.conf import settings

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = "__all__"

class PassedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passed
        fields = "__all__"


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"


class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}

