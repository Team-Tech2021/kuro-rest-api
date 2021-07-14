from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from subprocess import Popen
import subprocess
from editor_api.models import Code, Passed
from rest_framework.decorators import api_view
import urllib.parse


''' here we should use the request from search query to send test results as json'''
@api_view(['POST'])
def run_code(request):

    if request.method == 'POST':

            print(request.POST)
            code = request.data.get('code')
            code = urllib.parse.unquote(code)
            print('the code',code)
            problem = request.data.get("problem")
            print('here is no error')
            print('here is the request user' , request.user)
            try:
                Code.objects.get(user_id=request.user.id, problem_id=problem)
                Code.objects.filter(user_id=request.user.id, problem_id=problem).update(code=code)
            except:
                code_ = Code(user_id=request.user.id, problem_id=problem, code=code)
                code_.save()

            # solution = open("solution.py", mode="w")
            # solution.write(code)
            # solution.close()
            with open('solution.py', 'w') as file:
                file.write(code)

            out = Popen(["python", "-m", "unittest", "-q", f"test.A{problem}"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
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
                    Passed.objects.get(user_id=request.user.id, problem_id=problem)
                except:
                    passed = Passed(user_id=request.user.id, problem_id=problem)
                    passed.save()
            return JsonResponse(data= data , safe =False)


@api_view(['GET'])
def is_passed(request):
    problem = request.GET['problem']
    try:
        Passed.objects.get(user_id=request.user.id, problem_id=problem)
        return HttpResponse(True,content_type="application/json")
    except:
        return HttpResponse(False,content_type="application/json")




@api_view(['POST'])
def select_code(request):
    # text
    problem = request.POST.get("problem")
    try:
        print('here is the Code',Code.objects.get(user_id=request.user.id, problem_id=problem))
        existing_code = Code.objects.get(user_id=request.user.id, problem_id=problem)
    except:
        existing_code = {}
        return HttpResponse(existing_code, content_type="application/json")
    print('here it is', existing_code)

    return HttpResponse(existing_code.code, content_type="application/json")


