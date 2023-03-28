from .models import *
from django import forms

class ClientForm(forms.ModelForm): #эта модель подключена к странице order_taxi для формы заказа.Пока все поля обязательные
    #time_order = forms.TimeField(widget=AdminTimeWidget()) #подсказчик выбора
    class Meta:

        model = Client    #наследование класса
        #fields = "__all__"  # все поля наследуем кроме тех которые заполняются автоматически
        fields = ['name','phone_number','email','comment']


