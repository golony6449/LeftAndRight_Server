from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# post
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# view function directory
from .view.find_relation import *

from .models import recentPost, press
import json

from .module.rss import Rss
from .module.crawler import Crawler
from .module.searchEngine import SearchEngine

# Create your views here.
def index(request):
    # return HttpResponse("This is article site.")
    return render(request, 'article/index.html')

@csrf_exempt
def search_relation(request):
    # 한겨레 모바일: http://211.233.22.224/
    # 조선일보 모바일 http://m.chosun.com/

    print("search request income")
    print('method: ', request.method)

    requestJson = None

    if request.method == 'OPTIONS':
        print(request.__dict__)
        response = HttpResponse()
        response['Access-Control-Request-Method'] = 'POST'
        return response

    if request.method == 'POST':
        print(request.body)

        requestJson = json.loads(request.body)

        # For Test
        print('keys: ', end='')
        for key in requestJson.keys():
            print(key, ' : ', requestJson[key], end='  ')
        print()

    result = find_relation(requestJson['journalism'], )

    return HttpResponse("Success")

@csrf_exempt
def search_by_keyword(request):
    requestJson = json.loads(request.body)
    responseDict = {}

    press = requestJson['journalism']
    keyword = requestJson['keyword']

    # TODO; Logging 기능 추가
    print(keyword)

    print('index 1 obj: ', recentPost.objects.get(keyword1=keyword))
    responseDict['result'] = recentPost.objects.get(keyword1=keyword).title

    # return HttpResponse("This function is now DEVELOP")
    responseDict['message'] = 'This function is now DEVELOP'

    return JsonResponse(responseDict)

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

def try_crawl(request):
    return render(request, 'article/crawl.html')

def crawl(request):
    print('cron"s work start!')
    response = {}

    crawler = None
    pressObj = None

    if request.POST['press'] == 'chosun':
        crawler = Crawler('chosun')
        pressObj = press.objects.get(name='chosun')
    else:
        crawler = Crawler('hani')
        pressObj = press.objects.get(name='hani')

    postInfo = crawler.scrap(request.POST['target'])

    print(postInfo)

    print('scrapping complete')

    query = recentPost(name=pressObj, title=postInfo['title'], url=postInfo['url'])

    # TODO: 반복문으로 이쁘게 만들수 없을까?
    # query.set_keywords(postInfo['word_count'])

    query.keyword1, _ = postInfo['word_count'][0]
    query.keyword2, _ = postInfo['word_count'][1]
    query.keyword3, _ = postInfo['word_count'][2]
    query.keyword4, _ = postInfo['word_count'][3]
    query.keyword5, _ = postInfo['word_count'][4]

    query.save()

    response = postInfo
    response['success'] = True

    return render(request, 'article/crawl_result.html', response)
@ csrf_exempt
def search_in_web(request):
    # Front-end와 협의 후 수정
    # press = request.POST['press']
    press = 'chosun'
    requestJson = json.loads(request.body)
    keyword = requestJson['keyword']

    if press == 'chosun':
        search_engine = SearchEngine(press)
        result = search_engine.do_search(keyword)

    elif press == 'hani':
        pass

    else:
        return HttpResponse('WrongPressName')

    response_dict = {}

    for idx in range(len(result)):
        index = str(idx)
        title, url = result[idx]
        response_dict[index] = {'title': title, 'url': url}

    return JsonResponse(response_dict)

# def login(request):
#     return render(request, 'article/login.html')
#
# def try_login(request):
#     print('id', request.POST['id'])
#     print('pw', request.POST['password'])
#     return HttpResponseRedirect(reverse('login'))

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