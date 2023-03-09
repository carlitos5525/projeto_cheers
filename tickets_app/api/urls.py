from django.urls import path
from tickets_app.api import views

urlpatterns = [
   path('lista/', views.tickets_list, name="lista-ingressos"),
   path('<int:id>', views.ticket_details, name="detalhes-ingresso"),
   path('cadastrar', views.ticket_create, name="criar-ingresso"),
   path('venda/<int:id>', views.ticket_sale, name="vender-ingresso"),
]