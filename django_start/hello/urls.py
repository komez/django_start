from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='hello'),
    path('index', views.index, name='index'),
    #path('form',views.form, name='form'),
]