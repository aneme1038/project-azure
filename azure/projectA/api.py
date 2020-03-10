from projectA.models import Item
from rest_framework import viewsets, permissions
from .serializers import ItemSerializer#, UserSerializer, GroupSerializer
'''
# A viewset allows us to create a full CRUD API without having to specify
# explicit methods for the functionality. It's kind of like how Ruby on Rails
# works with Resources.
# If you want to read more about it, visit
# https://django-rest-framework.org/api-guide/viewsets
'''
# Item Viewset
class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited
    """
    queryset = Item.objects.all()
    permission_classes = [
        #change this later to access only our own items
        permissions.AllowAny
    ]
    serializer_class = ItemSerializer

# # User Viewset
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# # Group Viewset
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited
#     """
