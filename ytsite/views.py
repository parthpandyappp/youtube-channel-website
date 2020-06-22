# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import form_submission

def index(request):
	return render(request, "ytsite/playlist.html")

def create_form(request):
	return render(request, "ytsite/upload.html")
# Create your views here. 
def created(request):
    if request.method == "POST" :
        form = form_submission()
        form.playlist = request.POST.get('playlist')
        form.card_name = request.POST.get('card_name')
        form.card_text = request.POST.get('card_details')
        form.photo = request.FILES['image']
        form.url = request.POST.get('link')
        form.save()
        usr = form_submission.objects.all()
        return render(request, "ytsite/created.html", {'usr' : usr})

def mechtech(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/mech_tech.html", {'usr' : usr})


def comptech(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/comp_tech.html", {'usr' : usr})


def tricktech(request):
    usr = form_submission.objects.all()
    return render(request, "ytsite/trick_tech.html", {'usr' : usr})


    """if(p.playlist=="Comp_tech"):
        print("ghus gaya")
        q = form_submission.objects.all().filter(playlist="Comp_tech")
        return render(request, "Comp_tech.html", {'q' : q})

    elif(p.playlist=="Mech_tech") :
        q = form_submission.objects.all().filter(playlist="Mech_tech")
        return render(request, "Mech_tech.html", {'q' : q})

    elif(p.playlist=="Comp_tech") :
        q = form_submission.objects.all().filter(playlist="Trick_tech")
        return render(request, "Trick_tech.html", {'q' : q})

    else :
        return render(request, "index.html", {'usr' : usr})"""