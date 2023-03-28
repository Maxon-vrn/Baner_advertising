from django.contrib import admin
from .models import *

class AdressAdvertisingAdmin(admin.ModelAdmin):
    list_display = ('id','address_banner','area','content','photo','photo1','photo2','photo3','photo4','is_published')
    list_display_links = ('id','address_banner','area','content','is_published')
    search_fields = ('address_banner', 'content')


class OrganizationAdmin(admin.ModelAdmin):  #error to makemigration on sait
    list_display = ('id','name_oranization','contact_face','logotip','phone_number','email','comment','is_published')
    list_display_links = ('id','name_oranization','contact_face','phone_number','email')
    search_fields = ('name_oranization', 'content')


# Register your models here.
admin.site.register(AdressAdvertising,AdressAdvertisingAdmin)
admin.site.register(Client)
admin.site.register(Organization,OrganizationAdmin)