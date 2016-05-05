from django.shortcuts import render,redirect
from django.http import HttpResponse
from article.models import UserProfile,HostProfile,host_stat
from datetime import datetime
# Create your views here.
from markdown import markdown

def tab(request):
    return render(request, "tab.html", )
def login(request):
    return  render(request,"login.html",{"password_prompt":""})
def create_account(request):
    return  render(request,"create_account.html")
def choose_all(request):
    return  render(request,"chooseall.html")
def scroll_menu(request):
    return  render(request,"scrollMenu.html")
def homework2(request):
    return  render(request,"homework2.html")

def edit_table(request):
    return render(request,"edittable.html",{"host_list":HostProfile.objects.all(),
                                            "host_stat":host_stat})

#处理登录用户名和密码验证
def login_handle(request):

    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        print(u,p)
        user = UserProfile.objects.filter(username=u)
        try:
            if p == user.first().password:
                return render(request,"tab.html")
            else:
                return render(request,"login.html",{"password_prompt":"Incorrect username or password."})
        except AttributeError:
            return render(request, "login.html", {"password_prompt": "Incorrect username or password."})

#注册
def register_handle(request):
    if request.method == "POST":
        UserProfile.objects.create(username = request.POST.get("username"),
                                   email=request.POST.get("emailaddress"),
                                   phone=request.POST.get("phonenumber"),
                                   password=request.POST.get("password"),
                                   )
        return redirect("/")


