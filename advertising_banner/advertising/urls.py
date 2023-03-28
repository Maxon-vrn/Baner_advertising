from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),   #адрес, функция обработчик, переменная -имя для работы
    path('application_accepted/', order, name='order'),    #форма успешной отправки данных
]