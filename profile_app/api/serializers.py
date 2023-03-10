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
    
    #id = serializers.IntegerField(read_only=True)
    #profile_name = serializers.CharField(max_length=255, required=True)
    #cpf = serializers.CharField(max_length=11, required=True)
    #email = serializers.EmailField(max_length=50, required=True)
    #password = serializers.CharField(max_length=255, required=True)
    #cellphone_number = serializers.CharField(max_length=14, required=True)
    #insta_profile = serializers.CharField(max_length=50, required=False, allow_blank=True)
    #is_active = serializers.BooleanField(read_only=True)
    
    #def create(self, validated_data):
    #   return User.objects.create(**validated_data)
   
    #def update(self, instance, validated_data):
     #   instance.profile_name = validated_data.get('profile_name', instance.profile_name)
     #   instance.cpf = validated_data.get('cpf', instance.cpf)
     #   instance.email = validated_data.get('email', instance.email)
     #   instance.password = validated_data.get('password', instance.password)
      #  instance.cellphone_number = validated_data.get('cellphone_number', instance.cellphone_number)
      #  instance.insta_profile = validated_data.get('insta_profile', instance.insta_profile)
      #  instance.save()
      #  return instance


    