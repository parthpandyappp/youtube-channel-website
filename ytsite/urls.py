from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('upload/', views.create_form, name='upload'),
    path('created/', views.created, name = "created"),
    path('comptech/', views.comptech, name = "comptech"),
    path('tricktech/', views.tricktech, name = "tricktech"),
    path('mechtech/', views.mechtech, name = "mechtech"),
    path('nodata/', views.nodata, name='nodata')
]
