from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# post
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Form for register
from .forms import RegisterForm

# view function directory
from .view.find_relation import *

# TODO: 에러발생 이유 파악
# from models import recentPost

from rest_framework.parsers import JSONParser

# Create your views here.
def index(request):
    # return HttpResponse("This is article site.")
    return render(request, 'article/index.html')

def login(request):
    return render(request, 'article/login.html')

def try_login(request):
    print('id', request.POST['id'])
    print('pw', request.POST['password'])
    return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def search_relation(request):
    # 한겨레 모바일: http://211.233.22.224/
    # 조선일보 모바일 http://m.chosun.com/

    print("search request income")
    print('method: ', request.method)

    if request.method == 'OPTIONS':
        print(request.__dict__)
        response = HttpResponse()
        response['Access-Control-Request-Method'] = 'POST'
        return response

    if request.method == 'POST':
        # print(JSONParser.parse(request))

        print(request.body)
        print('keys: ', end='')
        for key in request.POST.keys():
            print(key, end='  ')

    return HttpResponse("Success")

    result = find_relation()

    # TODO: html 작성
    return HttpResponse(request, 'article/list.html')

# For Test
def test(request):
    print('test request income')
    print('income method: ', request.method)
    print('request body: ', request.body)
    print('request data', request.data)

    if request.method == 'POST':
        print('keys: ', end='')
        for key in request.POST.keys():
            print(key, end='  ')

        return HttpResponse("Success")

    else:
        return render(request, 'article/test.html')

# # Case 1. generic view를 사용하지 않고 구현
# def register():
#     pass
#
# # Case 2.
# # TODO FormView를 이용한 구현
# # https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-editing/
# class RegisterView(generic.edit.FormView):
#     template_name = 'article/register_form.html'
#     form_class = RegisterForm
#     success_url = '/try_register/'
#
# def try_register():
#     pass
#
# class IndexView(generic.ListView):
#     template_name = 'article/index.html'
#     model = 'press'