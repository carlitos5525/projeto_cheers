from django.urls import path
from tickets_app.api import views

urlpatterns = [
   path('list/', views.tickets_list, name="lista-ingressos"),
   path('<int:id>', views.ticket_details, name="detalhes-ingresso"),
   path('create', views.ticket_create, name="criar-ingresso"),
]