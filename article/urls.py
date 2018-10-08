from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login', views.login, name='login'),
    # path('try_login', views.try_login, name='try_login'),
    path('test', views.test, name='test'),
    # path('register', views.register, name='register'),
    # path('register', views.RegisterView.as_view(), name='register'),
    # path('try_register', views.try_register, name='try_register'),
    path('find_relation/', views.search_relation, name='search_relation'),
    path('search', views.search_by_keyword, name='search_by_keyword'),
    path('try_crawl', views.try_crawl, name='try_crawl'),
    path('crawl', views.crawl, name='do_crawl'),
]