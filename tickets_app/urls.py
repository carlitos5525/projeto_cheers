from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.tickets_list, name="lista-ingressos")
]