from audioop import reverse

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class AdressAdvertising(models.Model):
    title = models.CharField(max_length=255)    #address banner
    content = models.TextField(blank=True)      #описание
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # don't work normal
        return reverse('post', kwargs={'post_id':self.pk})

    class Meta:
        verbose_name="Адреса баннеров"
        verbose_name_plural = "Адреса баннеров"
        ordering = ['time_create','title']

class Client(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True) #проверка номера на валидность через библиотеку
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Контакты клиентов"
        verbose_name_plural = "Контакты клиентов"
        ordering = ['time_create']