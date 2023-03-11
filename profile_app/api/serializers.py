from rest_framework import serializers
from profile_app.models import User
from tickets_app.api.serializers import TicketSerializer

class UserSerializer(serializers.Serializer):
        
    class Meta:
        model = User
        fields = "__all__"


class UserTicketsSerializer(serializers.Serializer):
    profile_name = serializers.CharField(max_length=255, required=True)
    cpf = serializers.CharField(max_length=11, required=True)
    email = serializers.EmailField(max_length=50, required=True)
    cellphone_number = serializers.CharField(max_length=14, required=True)
    insta_profile = serializers.CharField(max_length=50, required=False, allow_blank=True)
    is_active = serializers.BooleanField(read_only=True)
    seller_tickets = TicketSerializer(many=True, read_only=True)
    buyer_tickets = TicketSerializer(many=True, read_only=True)
    

    