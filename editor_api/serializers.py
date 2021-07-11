from rest_framework import serializers
from .models import Code , Passed , Profile , Problem


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = "__all__"

class PassedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passed
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"
