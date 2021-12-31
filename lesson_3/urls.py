from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/<str:name>', views.postpage, name='posts_list'),
    path('dz1/', views.dz1),
    path('dz/', views.Dz.as_view()),
    path('dz/<int:number>/', views.postpage),
    path('example-form/', views.ExampleFormView.as_view(), name='example_form'),
    path('example-form/success/', views.example_success, name='example_form_success'),
    path('urok6/', views.my_form)
]
