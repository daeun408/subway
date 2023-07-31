from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from common.forms import UserForm

# Create your views here.
def home(request):
    return render(request, 'common/home.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #화면 입력값 가져오기
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) # 자동 로그인
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('common:home')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})