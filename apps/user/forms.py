from django import forms
from django.core.exceptions import ValidationError
from .models import *

class LoginForm(forms.Form):
  username = forms.CharField(
    min_length=3,
    widget=forms.TextInput(
      attrs={"placeholder":"사용자명 (3자리 이상)"},
    ),
  )
  password = forms.CharField(
    min_length=4,
    widget=forms.PasswordInput(
      attrs={"placeholder":"비밀번호 (4자리 이상)"},
    ),
  )

class SignupForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)
  password_verify = forms.CharField(widget=forms.PasswordInput)
  profile_image = forms.ImageField()
  short_description = forms.CharField()

  def clean_username(self):
    username = self.cleaned_data['username']
    if CustomUser.objects.filter(username=username).exists():
      raise ValidationError(f"입력한 사용자명({username})은 이미 사용중입니다.")
    return username
  
  def clean(self):
    password = self.cleaned_data['password']
    password_verify = self.cleaned_data['password_verify']
    if password != password_verify:
      self.add_error('password_verify', '비밀번호와 비밀번호 확인란의 값이 다릅니다.')

  def save(self):
    username = self.cleaned_data['username']
    password = self.cleaned_data['password']
    profile_image = self.cleaned_data['profile_image']
    short_description = self.cleaned_data['short_description']
    user = CustomUser.objects.create_user(
      username = username,
      password = password,
      profile_image = profile_image,
      short_description = short_description,
    )
    return user