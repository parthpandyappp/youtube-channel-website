# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import form_submission

def index(request):
    posts = form_submission.objects.all()
    args = {'posts':posts}
    return render(request, "index.html", args)

def create_form(request):
	return render(request, "upload.html")

# def created(request):
#     p = request.FILES['image']
    
#     user = form_submission(photo = p)
#     user.save()
#     return render(request,"created.html")

def created(request):
	form = form_submission()
	form.card_name = request.POST.get('card_name')
	form.card_text = request.POST.get('card_details')
	form.url = request.POST.get('link')
	form.save()
	p = request.FILES['image']
	user = form_submission(photo = p)
	print("code in this line")
	user.save()
	return render(request, "created.html")
# # Create your views here.
