from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('try_login', views.try_login, name='try_login'),
    path('test', views.IndexView.as_view(), name='test'),
    # path('register', views.register, name='register'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('try_register', views.try_register, name='try_register'),
    path('find_relation',views.search_relation, name='search_relation'),
]