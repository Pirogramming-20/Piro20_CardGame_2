from django.shortcuts import render, redirect
from .forms import *
import random

def show_main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    else:
        return render(request, 'splashScreen.html')

def start_game(request):
    if request.method == 'GET':
        form = AttackForm(attacker=request.user.profile)
        context = {
            'form' : form
        }
        return render(request, 'cardgame/attack.html', context)
    
    elif request.method == 'POST':
        form = AttackForm(request.POST, attacker=request.user.profile)
        if form.is_valid():
            form.instance.attacker = request.user.profile
            form.instance.rule = random.choice(['GreaterWin', 'LesserWin'])
            form.save()
            return redirect("cardgame:game_list")
        
def cancel_game(request, pk):
    if request.method == 'POST':
        Game.objects.get(pk=pk).delete()
        return redirect("cardgame:game_list")

# Game의 id를 전달받아야함
def accept_game(request, pk):
    game = Game.objects.get(id=pk)
    
    if request.method == 'GET':
        form = DefendForm(instance=game)
        context = {
            'form': form,
            'pk': pk,
            'attacker_name': game.attacker.user.username,
        }
        return render(request, 'cardgame/counterattack.html', context)
    
    elif request.method == 'POST':
        form = DefendForm(request.POST, instance=game)
        if form.is_valid():
            form.instance.is_over = True
            form.instance.winner = evaluate_result(form, form.instance.rule)
            form.instance.attacker.save()
            form.instance.defender.save()
            form.save()
            return redirect('cardgame:game_detail', pk)

def evaluate_result(form, gamerule):
    if form.instance.attack_num == form.instance.defend_num:
        return None
    if gamerule == 'GreaterWin':
        if form.instance.attack_num > form.instance.defend_num:
            form.instance.attacker.score += form.instance.attack_num
            form.instance.defender.score -= form.instance.defend_num
            return form.instance.attacker
        else:
            form.instance.attacker.score -= form.instance.attack_num
            form.instance.defender.score += form.instance.defend_num
            return form.instance.defender
    else:
        if form.instance.attack_num < form.instance.defend_num:
            form.instance.attacker.score += form.instance.attack_num
            form.instance.defender.score -= form.instance.defend_num
            return form.instance.attacker
        else:
            form.instance.attacker.score -= form.instance.attack_num
            form.instance.defender.score += form.instance.defend_num
            return form.instance.defender

def show_list(request):
    as_attacker = Game.objects.filter(attacker__user = request.user)
    as_defender = Game.objects.filter(defender__user = request.user)
    games = as_attacker | as_defender
    games = games.order_by('is_over')
    context = {
        'gameList':games
    }
    return render(request, 'cardgame/gameList.html', context)

# def show_detail(request, pk):
#     game = Game.objects.get(pk=pk)
#     context = {
#         'game':game,
#     }
#     return render(request, 'cardgame/gameDetail.html', context)
def show_detail(request, pk):
    game = Game.objects.get(pk=pk)
    score_change = 0
    if game.is_over:
        if game.winner:
            if game.winner.user == request.user:
                score_change = game.attack_num
            else:
                score_change = -game.defend_num
        else:
            score_change = 0

    context = {
        'game': game,
        'score_change': score_change,
    }
    return render(request, 'cardgame/gameDetail.html', context)


def show_ranking(request):
    profiles = Profile.objects.order_by('-score')
    context = {
        'profiles':profiles,
    }
    return render(request, 'cardGame/ranking.html', context)
