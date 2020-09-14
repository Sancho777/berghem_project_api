from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from rest_framework.response import Response
from .core import *


class UserProfileManager(BaseUserManager):
    """Manager for client profiles"""

    def create_user(self, cliente, preco, valor, troco, password=None):
        """Create a new client profile"""
        if not cliente:
            raise ValueError('Você deve informar o nome do cliente')

        calculo = get_change_formated_for(preco, valor)

        user = self.model(cliente=cliente, preco=preco,
                          valor=valor, troco=calculo)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, cliente, preco, valor, troco, password=None):
        """Create and save a new superuser with given details"""
        user = self.create_user(cliente, preco, valor, troco, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    cliente = models.CharField(max_length=255, unique=True)
    preco = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    valor = models.DecimalField(max_digits=99, decimal_places=2, blank=True)
    troco = models.CharField(max_length=9999, null=True)
    is_activate = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'cliente'
    REQUIRED_FIELDS = ['preco', 'valor']

    def get_full_name(self):
        """Retrieve full name os user"""
        return self.cliente

    def __str__(self):
        """Return string representation of our user"""
        return self.cliente
