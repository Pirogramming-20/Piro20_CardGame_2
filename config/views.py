from django.shortcuts import redirect

def index(request):
  if request.user.is_authenticated:
    return redirect("/cardgame/history/")
  else:
    return redirect("/user/login/")