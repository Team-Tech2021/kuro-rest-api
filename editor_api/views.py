from django.http import JsonResponse, HttpResponseRedirect, HttpRequest, request
from .models import Problem

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Profile , Passed , Code
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


# problems = Problem.objects.all()

# def problems(request):
#     pros = PROBLEMS.copy()
#     # print(pros)
#     for i in pros:
#         try:
#             Passed.objects.get(user_id=request.user.id, problem_id=i["id"])
#             i["complete"] = "True"
#         except Passed.DoesNotExist:
#             i["complete"] = "False"
#     return JsonResponse(pros, safe=False)

# print(problems[0].description)

PROBLEMS = [
    {
        "id": 1,
        "title": "Nth Fibonacci Sequence",
        "description": "Write a program to compute nth number ",
        "starter": "def nth_fib(n):\n\tpass",
    },
    {
        "id": 2,
        "title": "Repeated Word",
        "description": "Write a function that accepts a lengthy string parameter.",
        "starter": "import re\n\t def repeated_word(string): \n\tpass",
    },
    {
        "id": 3,
        "title": "Insertion Sort",
        "description": "Implement insertion sort on a given array.\nConvert the pseudo-code into working code in your language \\n",
        "starter": "def insertion_sort(arr): \n\tpass",
    },
     {
        "id": 4,
        "title": "Merge Sort",
        "description": "Implement merge sort on a given array.\nConvert the pseudo-code into working code in your language \\n",
        "starter": "def merge_sort(arr): \n\tpass",
    }, 
      {
        "id": 5,
        "title": "Binary Search List",
        "description": "find out the index if the input value inside the input array using binary search",
        "starter": "def binary_search(arr,key): \n\tpass",
    },
       {
        "id": 6,
        "title": "Binary Search List",
        "description": "takes a list as an argument. Without utilizing any of the built-in methods available to your language, return a list with elements in reversed order.",
        "starter": "def insert_shift_list(arr, int): \n\tpass",
    },
   
]
