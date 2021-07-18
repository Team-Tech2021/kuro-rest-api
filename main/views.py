from django.shortcuts import render
from django.http import  HttpResponseRedirect
from rest_framework import status
from rest_framework.authtoken.models import Token
from main.models import User
from django.contrib.auth import  logout
from django.urls import reverse
from rest_framework import generics
from django.contrib.auth import login, authenticate
from main.serializers import UserSignUp , LoginSerializer
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, "/")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


class SignUpView(generics.CreateAPIView):
    # queryset = User.objects.all()
    # serializer_class = UserSignUp
    def post(self, request, format='json'):
        serializer = UserSignUp(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.RetrieveAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                token = Token.objects.create(user=user)
                json = LoginSerializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(LoginSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
