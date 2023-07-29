from django.urls import path
from . import views

app_name = 'xl'

urlpatterns = [
    path('', views.index, name='gen'),
]
