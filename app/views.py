import random
from django.views.generic import *
from django.shortcuts import render
from .forms import BMIForm
from .models import *

class BMICalculatorView(FormView):
    template_name = "index.html"
    form_class = BMIForm

    def form_valid(self, form):
        height = form.cleaned_data['height'] / 100  
        weight = form.cleaned_data['weight']
        bmi = round(weight / (height * height), 2)

        # Determine BMI category
        category = ""
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        # Fetch a random tip from the database
        tips = RandomPopUp.objects.all()
        random_tip = random.choice(tips).description if tips.exists() else "Stay hydrated and maintain a balanced diet!"

        return render(self.request, self.template_name, {
            'form': form,
            'bmi': bmi,
            'category': category,
            'random_tip': random_tip  # ✅ Ensure this is passed to the template
        })
        
class UnderweightTipsView(ListView):
    template_name = 'underweight_tips.html'
    model = UnderweightTip
    context_object_name = 'tips'
    
class UnderweightTipsView(ListView):
    template_name = 'overweight_tips.html'
    model = OverweightTip
    context_object_name = 'tips'

