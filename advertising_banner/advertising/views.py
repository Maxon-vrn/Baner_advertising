from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,Http404
from .models import *

# if ....:
#   ....
# else:
#   raise Http404() - вызывается функция обработчик исключения pageNotFound!

# return redirect('/') - перенаправление и куда

def index(request):     #главная страница
    address_banner = AdressAdvertising.objects.all()
    return render(request,'advertising/index.html', {'title':"Главная", 'posts': address_banner})

def contact(request):    #контакты для связи и адреса
    return render(request, 'advertising/contact.html')



def pageNotFound(request, exception):   #настроена обработка исключений 404
    return HttpResponseNotFound("<h1>Искомая страница не найдена на данном сервере.Попробуйте изменить запрос.</h1>")