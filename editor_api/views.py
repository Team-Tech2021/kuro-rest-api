from django.http import JsonResponse, HttpResponseRedirect, HttpRequest, request
from .models import Problem

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Profile , Passed , Code ,Test
# from .permissions import IsOwnerOrReadOnly
from .serializers import *


class ProfileList(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



class PassedList(ListCreateAPIView):
    queryset = Passed.objects.all()
    serializer_class = PassedSerializer


class PassedDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Passed.objects.all()
    serializer_class = PassedSerializer


class CodeList(ListCreateAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer


class CodeDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

class ProblemList(ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class ProblemDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class TestList(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Test.objects.all()
    serializer_class = TestSerializer
