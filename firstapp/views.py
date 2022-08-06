from django.shortcuts import render
from django.http import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def m404(request):
    return HttpResponseBadRequest('<h2>Error 404: bad request</h2')


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('About')


def contact(request):
    return HttpResponseRedirect('/about')


def details(request):
    return HttpResponsePermanentRedirect('/')


#def products(request, productid):
#    category = request.GET.get('cat', '')
#    output = "<h2>Продукт № {0}</h2><h3>Категория: {1}</h3>".format(productid, category)
#    return HttpResponse(output)


#def users(request):
#    id = request.GET.get('id', 1)
#    name = request.GET.get('name', 'Арсений')
#    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>".format(id, name)
#    return HttpResponse(output)

