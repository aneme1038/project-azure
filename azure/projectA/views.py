from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
# Create your views here.
def index(response):
    users = Users.objects.all()
    for user in users:
        print user.username_text
