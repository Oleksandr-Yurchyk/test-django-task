from django.urls import path

from . import views

urlpatterns = [
    path('en', views.index_en, name='index_en'),
    path('ua', views.index_ua, name='index_ua'),
    path('ru', views.index_ru, name='index_ru'),
]
