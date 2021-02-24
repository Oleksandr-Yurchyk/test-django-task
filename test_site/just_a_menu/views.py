from django.shortcuts import render


def index_en(request):
    return render(request, 'just_a_menu/homePageEN.html')


def index_ua(request):
    return render(request, 'just_a_menu/homePageUA.html')


def index_ru(request):
    return render(request, 'just_a_menu/homePageRU.html')
