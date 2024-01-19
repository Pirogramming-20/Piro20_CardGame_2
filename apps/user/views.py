from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from apps.user.forms import LoginForm, SignupForm

def login_view(request):
  if request.user.is_authenticated:
        return redirect('cardgame:game_list')  
  
  if request.method == 'POST':
    form = LoginForm(data=request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user:
        login(request, user)
        return redirect("cardgame:game_list")
      else:
        form.add_error(None, "입력하신 아이디를 가진 사용자가 없습니다!")
    context = {"form":form}
    return render(request, "user/login.html", context)
  else:
    form = LoginForm()
    context = {
      "form":form,
    }
    return render(request, "user/login.html", context)
  
def logout_view(request):
  logout(request)
  return redirect('cardgame:main_page')  # Redirect to the main page (splash screen for unauthenticated users)

def signup(request):
  if request.method == 'POST':
    form = SignupForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cardgame:game_list')  
  else:
    form = SignupForm()
  context = {"form":form}
  return render(request, 'user/signup.html', context)