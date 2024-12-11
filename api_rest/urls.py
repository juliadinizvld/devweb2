from django.urls import path
from . import views  # Importa as views definidas no arquivo views.py

urlpatterns = [
    path('', views.index, name='index'),  # URL principal
]