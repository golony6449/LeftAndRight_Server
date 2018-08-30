from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

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

def register():
    pass

def try_register():
    pass

class IndexView(generic.ListView):
    template_name = 'article/index.html'
    model = 'press'