from django.urls import path
from . import views

app_name = "instafetch"

urlpatterns = [
    path('', views.login, name="home"),
    path('index', views.index, name="index"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('addUser', views.addUser, name="addUser"),
    path('addPage', views.addPage, name="addPage"),
    path('fetch', views.fetch, name="fetch"),
    path('deletePage', views.deletePage, name="deletePage"),
    path('Success', views.success, name="success"),
]