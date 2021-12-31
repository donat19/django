from django.urls import path,re_path
from . import views

urlpatterns = [
    path('1/', views.index, name='index'),
    path('2/', views.second_view, name='second_page'),
    path('home/<str:username>', views.home, name='home-view'),
    re_path('book/<int:chapter>', views.book, name='book'),
    path('html1/', views.html1, name='html1')

]
