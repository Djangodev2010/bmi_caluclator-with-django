from django import forms

class BMIForm(forms.Form):
    height = forms.FloatField(label="Height (cm)")
    weight = forms.FloatField(label="Weight (kg)")