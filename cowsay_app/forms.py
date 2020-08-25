from django import forms

class TextForm(forms.Form):
    text = forms.CharField(max_length=100)