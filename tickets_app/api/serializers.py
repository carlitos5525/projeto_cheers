from rest_framework import serializers
from tickets_app.models import Ticket

class TicketSerializer(serializers.Serializer):
    
    
    id = serializers.IntegerField(read_only=True)
    is_available = serializers.BooleanField(read_only=True)
    is_sold = serializers.BooleanField(read_only=True)
    event_name = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=6)
    description = serializers.CharField(required=False, allow_blank=True)
    created_at = serializers.DateTimeField(read_only=True)
    sold_at = serializers.DateField(read_only=True)
    seller_id = serializers.PrimaryKeyRelatedField(read_only=True)
    buyer_id = serializers.PrimaryKeyRelatedField(read_only=True)
    
    
    def create(self, validated_data):
       return Ticket.objects.create(**validated_data)
   
    def update(self, instance, validated_data):
        instance.event_name = validated_data.get('event_name', instance.event_name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
        

