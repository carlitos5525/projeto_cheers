from datetime import date
from tickets_app.api.serializers import TicketSerializer
from tickets_app.models import Ticket
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
from tickets_app.api.permissions import TicketUserOrRearOnly


@api_view(['GET'])
def tickets_list(request):
    query_set = Ticket.objects.all().order_by('-created_at').filter(is_available=True)

    query_params = request.query_params
    if "event_name" in query_params:
        event_name_filter = query_params['event_name']
        query_set = query_set.filter(event_name__icontains=event_name_filter)
            
    if "price" in query_params:
        price_filter = query_params['price']
        query_set = query_set.filter(price=price_filter)
        
    if"created_at" in query_params:
        created_at_filter = query_params['created_at']
        query_set = query_set.filter(created_at__date=created_at_filter)
        
    serializer = TicketSerializer(query_set, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([TicketUserOrRearOnly ])
def ticket_details(request, id):
    
    try:
        ticket = Ticket.objects.get(pk=id)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ticket_create(request):
    serializer = TicketSerializer(data=request.data)
    
    seller = request.user
    
    if serializer.is_valid():
        serializer.save(seller_id=seller)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ticket_sale(request, id):
    try:
        ticket = Ticket.objects.get(pk=id)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    ticket.is_sold = True
    ticket.is_available = False
    ticket.sold_at = date.today()
    ticket.save()
    
    serializer = TicketSerializer(ticket)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
