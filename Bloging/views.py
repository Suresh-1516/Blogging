from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django. contrib import messages
from django.contrib import auth
from .forms import BlogpostForm
from .models import Like, Comment, Blogpost
from django.contrib.auth.decorators import login_required


def home(request):
    blog_list = Blogpost.objects.all()
    return render(request, "index.html", {'blogs': blog_list})

@login_required(login_url='log_in')
def trash(request, num):
    Blogpost.objects.filter(id=num).delete()
    return redirect(profile)

@login_required(login_url='log_in')
def blog(request, num):
    blog_title = Blogpost.objects.filter(id=num).values_list("title")
    blog_body = Blogpost.objects.filter(id=num).values_list("body")
    blog_comment = Comment.objects.filter(comment_blog_id=num).values_list("comment_string","comment_user")
    username = request.user.username
    like =  Like.objects.filter(liked_blog_id=num,liked_blog_user=username).exists()
    like_count =  Like.objects.filter(liked_blog_id=num).count()
    return render(request, 'blog_list.html', {"blog_title": blog_title[0][0], "blog_body": blog_body[0][0], "id": num,"comment":blog_comment,"like":like,"likes":like_count})

def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='log_in')
def post(request):

    form = BlogpostForm
    mydict = {
        'form': form
    }
    return render(request, "post.html", context=mydict)


@login_required(login_url='log_in')
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogpostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        return redirect('post')


@login_required(login_url='log_in')
def dashboard(request):
    blog_list_for = Blogpost.objects.all()
    return render(request, "dashboard.html", {'blogs': blog_list_for})


@login_required(login_url='log_in')
def profile(request):
    username ="@"+request.user.username
    blog_list_for = Blogpost.objects.filter(blog_user=username).all()
    return render(request, "profile.html", {'blogs': blog_list_for})

def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect username or password!')

    return render(request, "login.html")


def sign_in(request):

    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

            user = User.objects.filter(username=username).exists()
            if user is True:
                messages.error(request, 'Username already exists !')
            else:
                User.objects.create_user(username, email, password)
                return redirect('log_in')

    except Exception as e:
        print(e)
    return render(request, "sign_in.html")

@login_required(login_url='log_in')
def comment(request,id):
    try:
        if request.method == 'POST':
            comment = request.POST.get('comment')
            id = id
            username = request.user.username
            Comment.objects.create(comment_blog_id=id,comment_string=comment,comment_user=username)
            return redirect("blog",id)

    except Exception as e:
        print(e)
    
    return HttpResponse("Error 404 !")

@login_required(login_url='log_in')
def likes(request,id,status):
    try:
        username =  request.user.username
        if status == "True":
            Like.objects.create(liked_blog_id=id,liked_blog_user=username)
            return redirect("blog",id)
        if status == "False":
            Like.objects.filter(liked_blog_id=id,liked_blog_user=username).delete()
            return redirect("blog",id)

    except Exception as e:
        print(e)
    return HttpResponse("Error 404 !")

