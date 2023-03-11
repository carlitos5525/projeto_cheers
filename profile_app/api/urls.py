from django.urls import path
from profile_app.api import views

urlpatterns = [
   path('ingressos/', views.user_tickets_list),
]