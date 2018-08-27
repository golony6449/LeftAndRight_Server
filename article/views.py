from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is article site.")
    return render(request, 'article/index.html')