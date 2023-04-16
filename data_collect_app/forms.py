from django import forms

class CollectForms(forms.Form):
    name = forms.CharField(max_length=50, label='Full Name')
    team = forms.CharField(max_length=50, label='Team Name')
    age = forms.CharField(max_length=3, label='Age')