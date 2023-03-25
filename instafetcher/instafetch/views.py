from django.shortcuts import render
from .models import User, Page


# Create your views here.
def index(request):
    try:  # get email and password post data
        email = request.POST['email']
        password = request.POST['password']
        context = {'email': email}
    except:  # no email and/or password post data received
        context = {'message': 'No password/email post data received'}
        return render(request, 'instafetch/login.html', context)

    try:  # get the user object
        userObj = User.objects.get(email=email)
    except:
        context = {'message': f'No such user {email} exists'}
        return render(request, 'instafetch/login.html', context)

    if(not userObj.password == password):  # email and password don't match
        context = {'message': f'Incorrect password for user {email}'}
        return render(request, 'instafetch/login.html', context)
    else:
        context ={'pages': Page.objects.filter(user=userObj)
                   }
        return render(request, 'instafetch/index.html', context)


def login(request):
    return render(request, 'instafetch/index.html')

def addUser(request):
    if request.method=="POST":
        user = User()
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.save()
        return render(request, 'instafetch/login.html')
    else:
        return render(request, 'instafetch/login.html')

def signup(request):
    return render(request, 'instafetch/signup.html')

def addPage(request):
    pass

def fetch(request):
    pass

