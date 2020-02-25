from django.contrib import admin
from .models import Item

admin.site.site_header = "WorkFlow Application Admin"
admin.site.site_title = "WorkFlow Admin Area"
admin.site.index_title = "Welcome to the WorkFlow admin area"

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['item_title']}),
    (None, {'fields': ['item_text']}),
    ('Date Information', {'fields': ['creation_date'], 'classes': ['collapse']}),]

# Register your models here.
#can add multiple models in below statement.
admin.site.register(Item)
