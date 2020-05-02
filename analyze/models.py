from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.



class Report(models.Model):
    headline = models.CharField(max_length=250, default="Report")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #one to many relationship with user (one user has multiple reports)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse("report-detail", kwargs={"pk": self.pk})
    
    

    
