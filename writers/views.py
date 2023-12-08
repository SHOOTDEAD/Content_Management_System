from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as enter, logout as exit


#Render home page
def home_page(request):
    temp = request.session.get("status")
    request.session["status"] = 0
    return render(request, "home_page.html", context={"status": temp})

#Create user
def signup(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        form.is_valid()
        data = form.cleaned_data
        if data["password"] != data["re_enter"]:
            return render(request, "signup.html", context={"form": form, "status": 2})
        if User.objects.filter(username=data["username"]):
            return render(request, "signup.html", context={"form": form, "status": 1})
        else:
            data.pop('re_enter')
            user = User.objects.create_user(**data)
            user.save()
            request.session["status"] = 3
            return redirect("home")

    return render(request, "signup.html", context={"form": form})

#Login a user
def login(request):
    form = LoginForm(request.POST or None)
    request.session["status"] = 1
    if request.method == "POST":
        form.is_valid()
        data = form.cleaned_data
        user = authenticate(request, username=data["username"], password=data["password"])

        
        if user:
            enter(request, user)

            return redirect(reverse("articles"))
        return render(request, "login.html", context={"status": 2, "form": form})
    return render(
        request, "login.html", context={"form": form, "status": request.session["status"]}
    )

#logout user
def logout(request):
    if request.user.is_authenticated:
        exit(request)
        request.session["status"] = 2

        return redirect("home")
    else:
        request.session["status"] = 3
        return redirect("login")
    
