from django.db import models

# Create your database models here.

# Testing Classes - Aaron
class Users(models.Model):
    username_text = models.CharField(max_length=200)
    password_text = models.CharField(max_length=25)

def __str__(self):
    return self.alt_text
