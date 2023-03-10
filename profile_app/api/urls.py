from django.urls import path
from profile_app.api import views

urlpatterns = [
   path('<int:id>', views.user_tickets_list),
]