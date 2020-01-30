# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:01:44 2020

@author: jamie
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about' )
]