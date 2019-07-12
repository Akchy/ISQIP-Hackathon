from __future__ import unicode_literals

from django.db import models

CAT_CHOICES = (
    ('equip','Equipments'),
    ('cloth', 'Cloths'),
    ('book','Books'),
    ('toy','Toys'),
)

class Document(models.Model):
    name=models.CharField(max_length=25,blank=False)
    email=models.EmailField(max_length=25,blank=False)
    phrase=models.CharField(max_length=25,blank=False)
    categories = models.CharField(max_length=15, choices=CAT_CHOICES, default='green',blank=False)
    phone=models.IntegerField(blank=False)
    address=models.CharField(max_length=255,blank=False)
    description = models.CharField(max_length=255, blank=False)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
