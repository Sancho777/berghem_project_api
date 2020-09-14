from rest_framework import serializers
from profiles_api import models
from rest_framework.response import Response


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a client profile object"""

    class Meta:
        model = models.UserProfile
        fields = ['id', 'cliente', 'preco', 'valor', 'troco']
        read_only_fields = ['troco']

    def create(self, validated_data):
        """Create and return a new client"""
        user = models.UserProfile.objects.create_user(
            cliente=validated_data['cliente'],
            preco=validated_data['preco'],
            valor=validated_data['valor'],
            troco="Sem troco."
        )

        return user
