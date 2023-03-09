from tickets_app.api.serializers import TicketSerializer
from tickets_app.models import Ticket
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def tickets_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def ticket_details(request, id):
    ticket = Ticket.objects.get(pk=id)
    
    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    if request.method == 'DELETE':
        ticket.delete()
        return Response()


@api_view(['POST'])
def ticket_create(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

    

    