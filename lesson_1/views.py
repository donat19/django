from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', context={
        'hello_world': 'Hello World!',
        'urls': ['127.0.0.1:59/lesson_1/2/']
    })


def second_view(request):
    return HttpResponse('Second page! <br>'
                        + 'First page URL: <br>'
                        + 'http://127.0.0.1:59/lesson_1/1/')


def home(request, username):
    return HttpResponse(f'вы на домашней страничке, привет:{username}')


def book(request, chapter):
    return HttpResponse(f'вы на {chapter} главе\n, для того чтобы вернуться на главную страницу,нажмите\n '
                        f'http://127.0.0.1:59/lesson_1/home/')

def html1(request):
    return render(request,'index')