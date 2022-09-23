import requests
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import UserLoginForm


def user_login(reuqest):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(requests,user)
                return redirect('article:article_list')
            else:
                return HttpResponse('账号密码输入有误')
        else:
            return HttpResponse('输入不合法')
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form':user_login_form}
        return render(request, 'userprofiel/login.html', context)
    else:
        return HttpResponse('请使用post或者get')
