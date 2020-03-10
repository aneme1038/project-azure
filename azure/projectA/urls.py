#created file to create paths for linking our templates folder and its subsequent Files (REACT files)
#need line to get path
'''
from django.urls import path, include
from django.contrib import admin

#import views
from . import views

app_name = 'projectA'
urlpatterns = [
    path('', views.index, name='index'),
    #pass in any other views below..
]
'''
#Above selection is old code

#Below selection is new code
from rest_framework import routers
from .api import ItemViewSet

router = routers.DefaultRouter()
router.register('api/item', ItemViewSet, 'item')

urlpatterns = router.urls
