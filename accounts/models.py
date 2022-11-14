from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField()
    name = models.CharField(default = "", max_length = 20)
    password = models.CharField(max_length = 30, default = "")

    def __str__(self):
        return self.user.username