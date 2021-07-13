from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, BasePermission , AllowAny

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Passed , Code
from .serializers import *


class UserWritePermission(BasePermission):
    message = 'Editing code is restricted to the owner only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user



class PassedList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Passed.objects.all()
    serializer_class = PassedSerializer


class PassedDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [UserWritePermission]
    queryset = Passed.objects.all()
    serializer_class = PassedSerializer


class CodeList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Code.objects.all()
    serializer_class = CodeSerializer


class CodeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [UserWritePermission]
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

class ProblemList(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class ProblemDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

