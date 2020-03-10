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
from django.urls import path, include
from .api import ItemViewSet#, UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register('api/item', ItemViewSet, 'item')
# router.register('api/users', UserViewSet, 'user')
# router.register('api/groups', GroupViewSet, 'group')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
