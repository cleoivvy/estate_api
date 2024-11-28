from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('properties/', PropertyList.as_view(), name='property-list'),
    path('property/<int:pk>/', PropertyDetail.as_view(), name='property-detail'),
    path('add_to_favorites/<int:property_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/', favorites_list, name='favorites_list')
]