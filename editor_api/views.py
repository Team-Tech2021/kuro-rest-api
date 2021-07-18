from django.http import JsonResponse, HttpResponseRedirect, HttpRequest, request
from .models import Problem

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import  Passed , Code ,Test
from .permissions import IsOwnerOrReadOnly
from .serializers import *


class PassedList(ListCreateAPIView):
    queryset = Passed.objects.all()
    serializer_class = PassedSerializer


class PassedDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Passed.objects.all()
    serializer_class = PassedSerializer


class CodeList(ListCreateAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer


class CodeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

class ProblemList(ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class ProblemDetail(RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class TestList(ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Test.objects.all()
    serializer_class = TestSerializer

