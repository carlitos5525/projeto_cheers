from django.shortcuts import render
from tickets_app.models import Ticket
from django.http import JsonResponse

def tickets_list(request):
    tickets = Ticket.objects.all()
    data = {
        'tickets': list(tickets.values())
    }
    return JsonResponse(data)