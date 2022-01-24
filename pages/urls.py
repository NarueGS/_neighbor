from django.urls import path

from main.models import Despesas_Unidades
from .import views
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('Inquilinos_List', views.Inquilinos_list, name='il'),

]