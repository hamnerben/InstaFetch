from django.shortcuts import render
from .models import User, Page
import instaloader
import datetime
import yagmail

# Create your views here.
def index(request):
    try:  # get email and password post data
        email = request.POST['email']
        password = request.POST['password']
        context = {'email': email}
    except:  # no email and/or password post data received
        context = {'error_message': 'No password/email post data received'}
        return render(request, 'instafetch/login.html', context)

    try:  # get the user object
        userObj = User.objects.get(email=email)
    except:
        context = {'error_message': f'No such user {email} exists'}
        return render(request, 'instafetch/login.html', context)


    if(not userObj.password == password):  # email and password don't match
        context = {'error_message': f'Incorrect password for user {email}'}
        return render(request, 'instafetch/login.html', context)
    else:
        context ={'pages': Page.objects.filter(user=userObj)
                   }
        return render(request, 'instafetch/index.html', context)


def login(request):
    return render(request, 'instafetch/login.html')

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

    ## send email
    yag = yagmail.SMTP("instafetch455@gmail.com", "wdewxcbfitmbdijm")
    posts = getImages("shitheadsteve")
    content = """
    <h1>Hello there</h1>
    """
    for path in posts:
        content += f'<img src="{path}">'

    yag.send(to='instafetch455@gmail.com', subject='Your instafetch update', contents=content)
    return render(request, "instafetch/login.html")


def getImages(username):
    L = instaloader.Instaloader()
    L.login("instafetch455@gmail.com", "BenSpencer2Nathan!")
    profile = instaloader.Profile.from_username(L.context, username)
    recent_posts = []
    now = datetime.datetime.now()
    one_hour_ago = now - datetime.timedelta(hours=12)
    for post in profile.get_posts():
        if post.date > one_hour_ago:
            recent_posts.append(post.url)
        else:
            break
    return recent_posts
