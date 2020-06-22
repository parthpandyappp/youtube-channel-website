from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.create_form, name='upload'),
    path('created/', views.created, name = "created"),
    path('comptech/', views.comptech, name = "comptech"),
    path('tricktech/', views.tricktech, name = "tricktech"),
    path('mechtech/', views.mechtech, name = "mechtech"),
]