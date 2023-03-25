from django.urls import path
from . import views

app_name = "instafetch"

urlpatterns = [
    path('', views.index, name="home"),
    path('index', views.index, name="index"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('add', views.add, name="add"),
    path('fetch', views.fetch, name="fetch"),
]