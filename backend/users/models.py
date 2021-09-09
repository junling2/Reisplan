from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from itineraries.models import Itinerary

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_admin(self, email, password, name, **other):
        other.setdefault('is_admin', True)

        if other.get('is_admin') is not True:
            return ValueError("Admin Account must have is_admin True")

        return self.create_user(email, password, name, **other)

    def create_user(self, email, password, name, **other):
        if not email:
            raise ValueError("Must provide valid email")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **other)
        user.set_password(password)
        user.save()

        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    itineraries = models.ManyToManyField(Itinerary)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self) -> str:
        return self.name + " " + self.email