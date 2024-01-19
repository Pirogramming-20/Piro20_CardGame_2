from .models import *
from django import forms


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

class DefendForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["defend_num"]
        labels = {"defend_num": "내가 고른 카드"}
