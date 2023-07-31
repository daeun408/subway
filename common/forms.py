from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):  #UserCreationForm 상속
    email = forms.EmailField(label="이메일")  #속성 추가
    class Meta:
        model = User
        fields = ['username', 'email']