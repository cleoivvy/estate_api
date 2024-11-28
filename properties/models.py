from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.contrib.auth.models import User


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=200, default="user")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
    
    objects = UserManager()



class Property(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    square_footage = models.IntegerField(default=300)
    bedrooms = models.IntegerField(default=2)
    bathrooms = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.address}, {self.city}"
    
class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        unique_together = ('user', 'property')

    def __str__(self):
        
        return f"{self.user.email} favorite property: {self.property.address}"

   
