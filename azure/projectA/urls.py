#created file to create paths for linking our templates folder and its subsequent Files (REACT files)
#need line to get path
from django.urlls import path
#import views
from . import views

app_name = 'projectA'
urllpatterns = [
    path('', views.index, name='index'),
    #pass in any other views below..
]
