from django.urls import path
from . import views

# Django-rest-swagger
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', views.index, name='index'),
    # path('login', views.login, name='login'),
    # path('try_login', views.try_login, name='try_login'),
    path('test', views.test, name='test'),
    # path('register', views.register, name='register'),
    # path('register', views.RegisterView.as_view(), name='register'),
    # path('try_register', views.try_register, name='try_register'),
    path('find_relation/',views.search_relation, name='search_relation'),
    # django-rest-swagger
    url('rest-swagger', schema_view),

]