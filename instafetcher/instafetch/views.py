from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from instaloader import ProfileNotExistsException
from django.urls import reverse


from .models import User, Page, Login
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
        context['linked_page_list'] = Page.objects.filter(user=userObj)

        return render(request, 'instafetch/index.html', context)


def login(request):
    return render(request, 'instafetch/login.html')

def addUser(request):
    if request.method=="POST":
        user = User()
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.save()
        return HttpResponseRedirect(reverse('instafetch:login'))
    else:
        return render(request, 'instafetch/login.html')

def signup(request):
    return render(request, 'instafetch/signup.html')

def addPage(request):
    try:  # get email post data
        email = request.POST['email']
    except:
        context = {'error_message': 'No email post data received'}
        return render(request, 'instafetch/error.html', context)

    try:
        userObj = User.objects.get(email=email)
    except:
        context = {'error_message': 'No email post data received'}
        return render(request, 'instafetch/error.html', context)
    try:
        L = instaloader.Instaloader()
        loginInfo = Login.objects.get(email="instafetch456@gmail.com")
        L.login(loginInfo.email, loginInfo.password)
        username = request.POST["username"]
        profile = instaloader.Profile.from_username(L.context, username)

    except ProfileNotExistsException:
        context = {'error_message': f"The account {username} does not exist."}
        return render(request, 'instafetch/error.html', context)

    #  add the page to the database
    page = Page()
    page.username = username
    page.user = userObj
    page.save()

    return HttpResponseRedirect(reverse('instafetch:index'))


def fetch(request):

    ## send email


    yag = yagmail.SMTP("instafetch455@gmail.com", "wdewxcbfitmbdijm")
    posts = getImages("shitheadsteve")
    content = """
    <h1>Hello there</h1>
    """
    for path in posts:
        content += f'<img src="{path}">'
        content += posts[path]

    yag.send(to='instafetch455@gmail.com', subject='Your instafetch update', contents=content)
    return render(request, "instafetch/login.html")


def getImages(username):
    L = instaloader.Instaloader()
    loginInfo=Login.objects.get(email = "instafetch456@gmail.com")
    L.login(loginInfo.email, loginInfo.password)
    try:
        profile = instaloader.Profile.from_username(L.context, username)

    except ProfileNotExistsException:
        print(f"The account {username} does not exist.")

    recent_posts = {}
    now = datetime.datetime.now()
    one_hour_ago = now - datetime.timedelta(hours=12)
    for post in profile.get_posts():
        if post.date > one_hour_ago:
            recent_posts[post.url] = post.caption
        else:
            break
    return recent_posts

def deletePage(request):
    if request.method == "POST":
        page_id = request.POST.get('page_id')
        email = request.POST['email']
        context = {'email': email}
        try:  # get the user object
            userObj = User.objects.get(email=email)
        except:
            context = {'error_message': f'No such user {email} exists'}
            return redirect(request, 'instafetch/login.html', context)
    Page.objects.filter(id=page_id).delete()

    context['linked_page_list'] = Page.objects.filter(user=userObj)
    previous_url = request.META.get('HTTP_REFERER', context)
    return redirect(previous_url)
    #return render(request, 'instafetch/index.html', context)
    # previous_url = request.META.get('HTTP_REFERER', None)
    # if previous_url:
    #     return redirect(previous_url)
    # else:
    #     return redirect(reverse('instafetch:index'))
