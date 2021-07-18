from django.http import HttpResponse, JsonResponse
from subprocess import Popen
import subprocess
from editor_api.models import Code, Passed ,Test
from rest_framework.decorators import api_view
import urllib.parse


@api_view(['POST'])
def run_code(request):
    '''
    taken the encoded code and the user id and return the test result of the code and added it to passed table if the result is pass
    '''
    if request.method == 'POST':

            code = request.data.get('code')
            code = urllib.parse.unquote(code)
            problem = request.data.get("problem")

            try:
                print(Code.objects.all())
                Code.objects.get(user_id=request.user.id, problem_id=problem)
                Code.objects.filter(user_id=request.user.id, problem_id=problem).update(code=code)
            except:
                code_ = Code(user_id=request.user.id, problem_id=problem, code=code)
                code_.save()

            with open('solution.py', 'w') as file:
                file.write(code)

            try:
                test = Test.objects.get(problem_id=problem)
                with open('test.py', 'w') as file:
                    file.write(test.code)
            except:
                return  JsonResponse(data= f"the test for this problem{problem} doesn't exist" , safe =False)


            out = Popen(["python", "-m", "unittest", "-q", "test"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
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



@api_view(['POST','PUT'])
def check_code(request):
    '''
    taken the encoded code and the user id and return the test result of the code and return pass=True to user if the result is pass
    '''
    if request.method == 'POST':

            code = request.data.get('code')
            code = urllib.parse.unquote(code)
            problem = request.data.get("problem")

            try:
                # user_code = Code.objects.get(user_id=request.user.id, problem_id=problem)
                print("found it")
                Code.objects.filter(user_id=request.user.id, problem_id=problem).update(code=code)
                print("finish")
            except:
                print("I am in the except")
                code_ = Code(user_id=request.user.id, problem_id=problem, code=code)
                code_.save()

            with open('solution.py', 'w') as file:
                file.write(code)

            try:
                test = Test.objects.get(problem_id=problem)
                with open('test.py', 'w') as file:
                    file.write(test.code)
            except:
                return  JsonResponse(data= f"the test for this problem{problem} doesn't exist" , safe =False)


            out = Popen(["python", "-m", "unittest", "-q", "test"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
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

            return JsonResponse(data= {"data": data , "pass" :passed} , safe =False)




@api_view(['GET'])
def is_passed(request):
    '''
    check if a relation between the user and a problem "the user solved the problem" exist
    '''
    problem = request.GET['problem']
    try:
        Passed.objects.get(user_id=request.user.id, problem_id=problem)
        return HttpResponse(True,content_type="application/json")
    except:
        return HttpResponse(False,content_type="application/json")




@api_view(['POST'])
def select_code(request):
    '''
    check if a previous code for a user exist then return it or return empty object/dict
    '''
    problem = request.POST.get("problem")
    try:
        existing_code = Code.objects.get(user_id=request.user.id, problem_id=problem)
    except:
        existing_code = {}
        return HttpResponse(existing_code, content_type="application/json")

    return HttpResponse(existing_code.code, content_type="application/json")




