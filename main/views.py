from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from main.models import User
from django.contrib.auth import  logout
from django.urls import reverse
from rest_framework import generics
from main.serializers import UserSignUp


# Create your views here.
def index(request):
    return render(request, "/")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUp
