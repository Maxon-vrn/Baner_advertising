from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *
from .forms import *

# if ....:
#   ....
# else:
#   raise Http404() - вызывается функция обработчик исключения pageNotFound!

# return redirect('/') - перенаправление и куда

def index(request):  # главная страница
    address_banner = AdressAdvertising.objects.all()    #забираем данные из формы для публикации
    contact_organization = Organization.objects.all()
    if request.method == "POST":            #отправляем данные в форму при выполнении условий валидности
        client = ClientForm(request.POST)
        if client.is_valid():
            client.save()
            return redirect('order')
        else:
            print('Error',client.errors)
    else:
        client = ClientForm()
    return render(request, 'advertising/index.html',
                  {'title': "Главная", 'posts': address_banner, 'organization': contact_organization, 'client': client})


def order(request): #redirect - work,but not name client in form
    # #перанправление после успешной отправки формы и возврат обратно
    #name = request.POST['name']
    return render(request, 'advertising/application_accepted.html')


def pageNotFound(request, exception):  # настроена обработка исключений 404
    return HttpResponseNotFound("<h1>Искомая страница не найдена на данном сервере.Попробуйте изменить запрос.</h1>")
