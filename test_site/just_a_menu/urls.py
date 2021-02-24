from django.urls import path
from django.views.generic import ListView

from .models import Menu

urlpatterns = [
    path('en',
         ListView.as_view(queryset=Menu.objects.filter(lang_switch='en'), template_name='just_a_menu/homePage.html')),
    path('ua',
         ListView.as_view(queryset=Menu.objects.filter(lang_switch='ua'), template_name='just_a_menu/homePage.html')),
    path('ru',
         ListView.as_view(queryset=Menu.objects.filter(lang_switch='ru'), template_name='just_a_menu/homePage.html')),
]
