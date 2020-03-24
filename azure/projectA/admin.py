from django.contrib import admin
from .models import Item

admin.site.site_header = "Azure Application Admin"
admin.site.site_title = "Project Azure Admin Area"
admin.site.index_title = "Welcome to the Project Azure admin area"

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['item_title']}),
    (None, {'fields': ['item_text']}),
    ('Date Information', {'fields': ['creation_date'], 'classes': ['collapse']}),]

# Register your models here.
#can add multiple models in below statement.
admin.site.register(Item)
