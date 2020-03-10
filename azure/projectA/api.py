from projectA.models import Item
from rest_framework import viewsets, permissions
from .serializers import ItemSerializer
'''
# A viewset allows us to create a full CRUD API without having to specify
# explicit methods for the functionality. It's kind of like how Ruby on Rails
# works with Resources.
# If you want to read more about it, visit
# https://django-rest-framework.org/api-guide/viewsets
'''
# Item Viewset
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    permission_classes = [
        #change this later to access only our own items
        permissions.AllowAny
    ]
    serializer_class = ItemSerializer
