from django import forms

from consumables.models import Consumable


class ConsumablesForm(forms.ModelForm):
    class Meta:
        model = Consumable
        fields = "__all__"
