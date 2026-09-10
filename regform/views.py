from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse('Добрый день! Это главная страница приложения regform')

def index_2(request):
  return HttpResponse('Имя: Виктория. Логин: @ViktoriiaChiern')

def create(request):
#  return HttpResponse('Тут должна быть форма')
  return render(request, 'news/create.html')