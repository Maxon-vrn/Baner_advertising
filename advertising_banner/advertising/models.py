from audioop import reverse

from django.db import models
from phonenumber_field.modelfields import *

# Create your models here.
class AdressAdvertising(models.Model):
    address_banner = models.CharField(max_length=255)    #address banner
    area = models.CharField(max_length=255,default=' ')
    content = models.TextField(blank=True)      #описание
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name='Фото',default=' ',blank=True) #сделать не обязательным полем
    photo1 = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name='Фото1',default=' ',blank=True)
    photo2 = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name='Фото2',default=' ',blank=True)
    photo3 = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name='Фото3',default=' ',blank=True)
    photo4 = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name='Фото4',default=' ',blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.address_banner

    def get_absolute_url(self): # don't work normal
        return reverse('post', kwargs={'post_id':self.pk})

    class Meta:
        verbose_name="Адреса баннеров"
        verbose_name_plural = "Адреса баннеров"
        ordering = ['time_create','address_banner']      #sort by

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField() #проверка номера на валидность через библиотеку
    email = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=500,blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Контакты клиентов"
        verbose_name_plural = "Контакты клиентов"
        ordering = ['time_create']

class Organization(models.Model):
    name_oranization = models.CharField(max_length=80)    #name_oranization
    contact_face = models.CharField(max_length=100,default=' ')     #contact people on organization - contact_face
    logotip = models.ImageField(upload_to="photos/%Y/%m/%d/",default=' ')     #logo organization
    phone_number = PhoneNumberField(blank=True)  # проверка номера на валидность через библиотеку
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=500,default=' ')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name_oranization


    class Meta:
        verbose_name = "Kontact"
        verbose_name_plural = "Данные нашей организации"
        ordering = ['time_create', 'name_oranization']  # sort by
