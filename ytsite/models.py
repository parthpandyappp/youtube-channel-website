# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class form_submission(models.Model):
	card_name = models.CharField(max_length=100)
	card_text = models.TextField()
	photo = models.ImageField(upload_to='cars')
	url = models.URLField(max_length=250)
# Create your models here.
