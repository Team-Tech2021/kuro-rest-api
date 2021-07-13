from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from subprocess import Popen
import subprocess ## To Get output from shell command
from editor_api.models import Code, Passed
from django.contrib.auth.decorators import login_required
from editor_api.views import PROBLEMS ##################################### will be changed later
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializers_class = UserSerializer


''' here we should use the request from search query to send test results as json'''
@csrf_exempt
# @login_required(redirect_field_name='home')
def run_code(request):
    serializer_class = CodeSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    if request.method == 'POST':
        print('it is a post request')
    print(request)
    print('heeeeeeeereeeeee')
    print(request.POST)
    code = request.POST.get("code")
    print('the code',code)
    problem = request.POST.get("problem")
    print('the problem',problem)
    print('here is no error')
    print('here is the request user' , request.user)
    # user_id = int(request.GET["user"])
    try:
        Code.objects.get(user_id=request.user.id, problem_id=problem)
        Code.objects.filter(user_id=request.user.id, problem_id=problem).update(code=code)
    except:
        code_ = Code(user_id=request.user.id, problem_id=problem, code=code)
        code_.save()

    solution = open("solution.py", mode="w")
    solution.write(code)
    solution.close()

    out = Popen(["python", "-m", "unittest", "-q", f"test.NthFib"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    stdout = out.communicate()
    '''
    the data is the test result we want to return "to send as api response"

    '''
    data = str(stdout).split("======================================================================")
    passed = False
    if data and len(data) == 1 :
        new_result = x = data[0].replace("\\n", " ")
        if 'ERROR' not in new_result and 'FAILED' not in new_result and 'OK' in new_result and 'Ran':
            passed = True

    if passed:
        try:
            exist = Passed.objects.get(user_id=request.user.id, problem_id=problem)
        except:
            passed = Passed(user_id=request.user.id, problem_id=problem)
            passed.save()
    return JsonResponse(data= data , safe =False)



from django.http import JsonResponse
def select_code(request):
    problem = int(request.GET["problem"])
    try:
        print('here is the Code',Code.objects.get(user_id=request.user.id, problem_id=problem))
        existing_code = Code.objects.get(user_id=request.user.id, problem_id=problem)
    except:
        existing_code = {}
    print('here it is', existing_code)

    return HttpResponse(existing_code.code, content_type="application/json")


