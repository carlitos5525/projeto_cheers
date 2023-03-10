from django.shortcuts import render
from datetime import date
from profile_app.api.serializers import UserTicketsSerializer
from profile_app.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def user_tickets_list(request, id):

    
    query_set = User.objects.get(id=id)
            
        
    serializer = UserTicketsSerializer(query_set)
    return Response(serializer.data, status=status.HTTP_200_OK)