from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    name=models.CharField(max_length=25,blank=True)
    email=models.CharField(max_length=25,blank=True)
    phone=models.CharField(max_length=25,blank=True)
    address=models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
