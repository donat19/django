from django.shortcuts import render
from django.views import View
from django.templatetags.static import static
from django.http import (HttpResponse, FileResponse, HttpResponseRedirect,
                         HttpResponseNotAllowed, JsonResponse)


class Basic(View):
    def get(self, request):
        return JsonResponse({1: 'Hello JSON World!'})


class File(View):
    def file(request):
        return FileResponse(open(__package__.split('.')[-1]
                                 + static('img/001.jpg'), "rb+"),
                            content_type="image/jpeg")


class Radirect(View):
    def radirect(request):
        return HttpResponseRedirect('https://lp508209.myflexbe.com/')


class Text(View):
    def text(request):
        return HttpResponse("hello World", content_type='text/plain')


def dz1(request):
    return HttpResponse("{'priority': 100, 'task': 'Составить список дел'}, {'priority': 150, 'task': 'Изучать Django'},{'priority': 1, 'task': 'Подумать о смысле жизни'}", content_type='text/plain')


def dz2(request):
    return HttpResponse("Добро пожаловать во вселенную звездных войн!\nВыберите страницу:\nЛюк\nЛея\nХан\n", content_type='text/plain')

def luke(request):
    return HttpResponse("Страница Люка:\nЛюк Скайуокер — один из главных персонажей вселенной «Звёздных войн», джедай, сынсенатора с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера", content_type='text/plain')


def leah(request):
    return HttpResponse("Страница Леи:Лея Органа — дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.", content_type='text/plain')