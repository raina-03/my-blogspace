from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Blog


def register(request):

    if request.method == "POST":

        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(email=email).exists():
            return render(request, "blog/register.html", {
                "error": "Email already registered"
            })

        User.objects.create_user(
            username=email,
            first_name=name,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "blog/register.html")


def user_login(request):

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):

            login(request, user)

            return redirect("home")

        return render(request, "blog/login.html", {
            "error": "Invalid email or password"
        })

    return render(request, "blog/login.html")


def home(request):

    blogs = Blog.objects.all()

    return render(request, "blog/home.html", {
        "blogs": blogs
    })


def add_blog(request):

    if request.method == "POST":

        title = request.POST["title"]
        content = request.POST["content"]
        image = request.FILES["image"]

        Blog.objects.create(
            title=title,
            content=content,
            image=image
        )

        return redirect("home")

    return render(request, "blog/add_blog.html")
def user_logout(request):
    logout(request)
    return redirect("login")
    





