from django.shortcuts import render
from datetime import date
from profile_app.api.serializers import UserTicketsSerializer
from profile_app.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_tickets_list(request):

    request_user = request.user
    query_set = User.objects.get(id=request_user.id)
            
        
    serializer = UserTicketsSerializer(query_set)
    return Response(serializer.data, status=status.HTTP_200_OK)