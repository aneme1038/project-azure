from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

#Get items and display them
def index(request):
    #get the latest published Item in your list
    latest_item_list = Item.objects.order_by('-creation_date')[:5]
    #put the list into an object for contextual display
    context = {'latest_item': latest_item}
    return render(request, 'templates/index.html', context)

#Show specific item and its content
# def item_info(request, item_id):
#     try:
#         item = Item.objects.get(pk=item_id)
#     except Item.DoesNotExist:
#         raise Http404("Item Does Not Exist")
#     return render(request, 'projectA/InsertUrlPathwayHere', { 'item': item})

#Create other views here
