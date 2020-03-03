#created file to create paths for linking our templates folder and its subsequent Files (REACT files)
#need line to get path
from django.urls import path, include
#import views
from . import views

app_name = 'projectA'
urlpatterns = [
    path('', views.index, name='index'),
    #pass in any other views below..
]
