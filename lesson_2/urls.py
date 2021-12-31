from django.urls import path, re_path
from . import views

urlpatterns = [
    path('text/', views.Text.as_view()),
    path('json/', views.Basic.as_view()),
    path('radirect/', views.Radirect.as_view()),
    path('file/', views.File.as_view()),
    path('dz1/', views.dz1)

]
