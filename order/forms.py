from django import forms
from order.models import Sandwich

class SandwichForm(forms.ModelForm):
    class Meta:
        model = Sandwich
        fields = ['menu', 'bread', 'cheese', 'tosting', 'vegetables', 'sauce']
        labels = {
            'menu' : '메뉴',
            'bread' : '빵',
            'cheese': '치즈',
            'tosting': '토스팅 유무',
            'vegetables': '야채',
            'sauce': '소스(최대3개)',
        }