from django import forms
from .models import Inventory


class Operations(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ('stocks_left','inventory_name')
