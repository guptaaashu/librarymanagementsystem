from django.db import models

# Create your models here.
class book(models.Model):
    author = models.TextField()
    name=models.TextField(null=True,blank=True)
    publisher = models.TextField(max_length = 40)
    typec = models.TextField()
    about = models.TextField()
    available = models.BooleanField(default=True)
    issuing_date = models.DateField(null =True, blank=True)
    returning_date= models.DateField(null =True, blank=True)





