from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class ChangeCalculator(viewsets.ModelViewSet):
    """Calculadora de Troco: Informe o nome do cliente, preço do produto e valor pago pelo cliente
       para que seja calculado o troco e a transação gravada em nosso banco de dados."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = ([])  # Disable for testing (TokenAuthentication,)
    # Disable for testing (permissions.UpdateOwnProfile,)
    permission_classes = ([])
    filter_backends = (filters.SearchFilter,)
    search_fields = ('cliente', 'preco',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
