from django.db import models
from django import forms
from django.contrib.auth.models import User
#from ipfs_storage import InterPlanetaryFileSystemStorage 
# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    visible = models.ManyToManyField(User)
    vislist = models.CharField(max_length=500,null = True)

    

#user = User.objects.all()
#values = [item.email for item in user]
#users = forms.MultipleChoiceField(choices = values)