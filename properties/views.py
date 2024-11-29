from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework_simplejwt.tokens import RefreshToken
from  django.contrib.auth import authenticate, logout
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUser
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    search_fields = ['first_name', 'last_name', 'email', 'role', 'password']
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            try:
                User.objects.create_user(**serializer.validated_data)
            except Exception as e:
                return Response({'error': str(e)}, status=400)
            
            data = {
                "message": "User created successfully"
            }   
            
            return Response(data, status=200)
        return Response(serializer.errors)
    
    
    
class LoginView(APIView):
    @swagger_auto_schema(method="post", request_body=LoginSerializer)
    @action(detail=True, methods=['post'])
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, email=serializer.validated_data['email'],
                                password = serializer.validated_data['password'])
            if user:
                try:
                    refresh_token = RefreshToken.for_user(user)
                    
                    data = {}
                    data['id'] = user.pk
                    data['first_name'] = user.first_name
                    data['last_name'] = user.last_name
                    data['access_token'] = str(refresh_token.access_token)
                    data['refresh_token'] = str(refresh_token)
                    
                    
                    return Response(data, status=200)
                except Exception as error:
                    return Response(
                        {
                            "error": f"{error}"
                        },
                        status=400
                    )
            else:
                
                data = {
                    "error": "invalid login credentials"
                }  
                return Response(data, status=401)
        else:
            data = {
                "error": serializer.errors
            }   
            return Response(data, status=400)      



class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
    permission_classes = [IsUser]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        queryset = super().get_queryset()
        city = self.request.GET.get('city', None)
        price_min = self.request.GET.get('price_min', None)
        price_max = self.request.GET.get('price_max', None)
        property_type = self.request.GET.get('property_type', None)
        latitude = self.request.GET.get('latitude', None)
        longitude = self.request.GET.get('longitude', None)
        address = self.request.GET.get('address', None)

        if city:
            queryset = queryset.filter(city=city)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        if property_type:
            queryset = queryset.filter(property_type__iexact=property_type)
        if latitude and longitude:
            queryset = queryset.filter(latitude=latitude, longitude=longitude)
        if address:
            queryset = queryset.filter(address__icontains=address)

        return queryset
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
    
    
    

class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer



@api_view(['POST'])
@login_required
def add_to_favorites(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, property=property)
    if created:
        return Response({"message": "Property added to favorites."}, status=201)
    return Response({"message": "Property already in favorites."}, status=200)

@api_view(['GET'])
@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)



class LogoutView(APIView):

        @swagger_auto_schema(method="post", request_body=LogoutSerializer)
        @action(detail=True, methods=['post'])
        def post(self, request):
            serializer = LogoutSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            try:
                
                token = RefreshToken(token=serializer._validated_data['refresh_token'])
                token.blacklist()
            
                
                return Response({"message": "logout successful"}, status=200)
            except Exception as error:
                print(error)
                return Response({"error": "failed to blacklist token"}, status=400)
            
            