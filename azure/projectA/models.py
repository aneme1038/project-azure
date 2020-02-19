from django.db import models

# Create your database models here.

# Testing Classes - Aaron
class First(models.Model):
    name_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Second(models.Model):
    name_text = models.ForeignKey(First, on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=200)
    counter = models.IntegerField(default=0)

def __str__(self):
    return self.alt_text
