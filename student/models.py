from django.db import models
from books.models import book
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
        roll_no = models.TextField()
        name = models.TextField(max_length = 40)
        stud_class = models.TextField()
        department = models.TextField()
        books_issued =models.ManyToManyField(book,blank=True,null=True)
        user= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
