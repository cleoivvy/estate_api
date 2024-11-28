from rest_framework import serializers
from .models import  *

from rest_framework import serializers
from django.contrib.auth import get_user_model




User = get_user_model()


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)
    class Meta:
        model = Favorite
        fields = ['id', 'property', 'created_at']
        
        


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])  
        user.save()
        return user        
        
        
class LoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField()        