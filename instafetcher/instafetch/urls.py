from django.urls import path
from . import views

app_name = "instafetch"

urlpatterns = [
    path('', views.index, name="home"),
]