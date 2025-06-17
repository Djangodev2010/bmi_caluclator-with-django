from django.urls import path
from .views import *

urlpatterns = [
    path('',  BMICalculatorView.as_view(), name='index'),
    
    path('underweight-tips', UnderweightTipsView.as_view(), name='underweight_tips'),
    
    path('overweight-tips', UnderweightTipsView.as_view(), name='overweight_tips'),
    
]

