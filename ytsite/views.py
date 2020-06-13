# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import form_submission

def index(request):
	return render(request, "index.html")

def create_form(request):
	return render(request, "upload.html")

def created(request):
	if request.method == 'POST':
		if request.POST.get('card_name') and request.POST.get('card_details') and request.POST.get('image') and request.POST.get('link'):
			form = form_submission()
			form.card_name = request.POST.get('card_name')
			form.card_text = request.POST.get('card_details')
			form.photo = request.POST.get('image')
			form.url = request.POST.get('link')
			form.save()
			return render(request, "created.html")
		else:
			return render(request, "created.html")
	return render(request, "created.html")
# Create your views here.
