from .models import *
from django import forms
import random

class AttackForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["attack_num", "defender"]
        labels = {"attack_num": "내가 고른 카드", "defender": "공격할 상대"}

    def __init__(self, *args, **kwargs):
        attacker = kwargs.pop("attacker", None)
        super(AttackForm, self).__init__(*args, **kwargs)
        if attacker:
            self.fields["defender"].queryset = Profile.objects.exclude(
                user=attacker.user)
        if not self.instance.attack_num:
            random_choices = sorted(random.sample(range(1, 11), 5))
            self.fields["attack_num"].choices = [(n, n) for n in random_choices]
    
class DefendForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["defend_num"]
        labels = {"defend_num": "내가 고른 카드"}

    def __init__(self, *args, **kwargs):
        super(DefendForm, self).__init__(*args, **kwargs)
        if not self.instance.defend_num:
            random_choices = sorted(random.sample(range(1, 11), 5))
            self.fields["defend_num"].choices = [(n, n) for n in random_choices]