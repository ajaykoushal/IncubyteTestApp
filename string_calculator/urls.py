from django.contrib import admin
from django.urls import path

# Import the calculator_view
from string_calculator.views import calculator_view


urlpatterns = [
    # Create a URL pattern to load the view
    path('', calculator_view, name='calculator'),
]
