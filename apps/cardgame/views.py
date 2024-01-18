from django.shortcuts import render, redirect

def show_base(request):
    return render(request, 'base.html')

def history(request):
    if not request.user.is_authenticated:
        return redirect("/user/login/")
    return render(request, "cardgame/history.html")