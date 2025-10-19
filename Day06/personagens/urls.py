from django.urls import path
from . import views

urlpatterns = [
    # Rota principal do app
    path('', views.lista_personagens, name='lista_personagens'),
]