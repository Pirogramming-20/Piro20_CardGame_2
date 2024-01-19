from django.shortcuts import render

def show_base(request):
    return render(request, 'base.html')