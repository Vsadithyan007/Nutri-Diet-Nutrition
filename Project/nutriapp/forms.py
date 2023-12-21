from django import forms
from .models import Nutri

class NutriForm(forms.ModelForm):
    class Meta:
        model = Nutri
        fields = '__all__'


class BMIForm(forms.ModelForm):
    class Meta:
        model = Nutri
        fields = ['Gender','Height','Weight']

class WeightForm(forms.ModelForm):
    class Meta:
        model = Nutri
        fields = ['Age','Gender','Height','Weight','LifeStyle']
        
