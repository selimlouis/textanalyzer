from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class Report(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #one to many relationship with user (one user has multiple reports)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    
