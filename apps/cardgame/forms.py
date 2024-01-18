from django import forms
from .models import *

class TempForm(forms.ModelForm):
    class Meta:
        model = TempGameModel
        fields = ('attacker_cards', 'defender_id')