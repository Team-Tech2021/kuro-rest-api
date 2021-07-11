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

# def problem_pass(request):
#     print(request)

#     # pros = .copy()
#     pros = Problem.objects.all()
#     for i in pros:
#         try:
#             Passed.objects.get(user_id=request.user.id, problem_id=i.id)
#             i["complete"] = "True"
#         except Passed.DoesNotExist:
#             i["complete"] = "False"
#     return JsonResponse(pros, safe=False)
# print(problem_pass(request))

# # print(problems[0].description)

PROBLEMS = [
    {
        "id": 1,
        "title": "Nth Fibonacci Sequence",
        "description": "<p>Write a program to compute nth number of a <a href=\"https://en.wikipedia.org/wiki/Fibonacci_number\">fibonacci number sequence</a>.</p><br>Starting Numbers: <code>nth_fib(1) = 0</code>, <code>nth_fib(2) = 1</code><br><br><p>Example Input & Output: </p><ul><li><code>nth_fib(2) = 1</code></li><li><code>nth_fib(6) = 5</code></li></ul><br><h4>Note:</h4><p>If you see a RecursionError, make sure you try again, the maximum number for input is 15.</p> <br><br><h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def nth_fib(n):\n\tpass",
    },
    {
        "id": 2,
        "title": "Palindrome Checker",
        "description": "Return True if the string is a <a href='https://en.wikipedia.org/wiki/Palindrome'>palindromic string</a> (same as you read it backward as forward), given with following constraints: <ul><li>Only check  the alphanumeric part of a string,</li><li>This is case insensitive, means that RaCeCar is a palindromic string.</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"race CAR\") = True</code></li><li><code>palindrome(\"2_A3*3#A2\") = True</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",

    }
]
