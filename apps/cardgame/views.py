from django.shortcuts import render
from .forms import *
import random

def show_main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    else:
        return render(request, 'splashScreen.html')

def start_game(request):
    if request == 'GET':
        initial_data = {
            'rule': random.choice(['GreaterWin', 'lesserWin']),
            'attacker_id': request.user.id
        }
        form = TempForm(initial=initial_data)
        context = {
            'form' : form
        }
        return render(request, 'attack.html', context)
    
    elif request == 'POST':
        


def accept_game(request):
    return