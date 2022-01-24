from django.shortcuts import render
from main.models import *


def home(request):
    return render(request, 'home.html')

def despesaF(request):
    
    f = Despesas_Unidades.objects.filter(Despesas_Unidades.unidade)
    return render(request, 'despesa_filtro.html',{'unidade':f})

def Inquilinos_list(request):
    l = Inquilinos.objects.all()
    return render(request, 'inquilinos_list.html',{'l':l})