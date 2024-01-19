from .models import *
from django import forms
import random

def get_random_choices():
    return sorted(random.sample(range(1, 11), 5))

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
            self.instance.attack_num = get_random_choices()
            self.fields["attack_num"] = forms.ChoiceField(choices=[(n, n) for n in self.instance.attack_num])
    
class DefendForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["defend_num"]
        labels = {"defend_num": "내가 고른 카드"}

    def __init__(self, *args, **kwargs):
        super(DefendForm, self).__init__(*args, **kwargs)
        if not self.instance.defend_num:
            self.instance.defend_num = get_random_choices()
            self.fields["defend_num"] = forms.ChoiceField(choices=[(n, n) for n in self.instance.defend_num])