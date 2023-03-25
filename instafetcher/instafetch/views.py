from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'instafetch/index.html')

def login(request):
    return render(request, 'instafetch/login.html')

def signup(request):
    return render(request, 'instafetch/signup.html')

def addPage(request):
    pass

def fetch(request):
    pass

