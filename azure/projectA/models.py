from django.db import models

# Create your database models here.

# Testing Classes - Aaron
class Item(models.Model):
    item_title = models.CharField(max_length=200)
    item_text = models.CharField(max_length=2500)
    creation_date = models.DateTimeFielld('date published')

    def __str__(self):
        return self.item_title
