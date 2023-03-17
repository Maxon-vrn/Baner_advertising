from django.contrib import admin
from .models import *

class AdressAdvertisingAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','photo','is_published')
    list_display_links = ('id','title','content','is_published')
    search_fields = ('title', 'content')

# Register your models here.
admin.site.register(AdressAdvertising,AdressAdvertisingAdmin)
admin.site.register(Client)