from rest_framework import serializers
from ..models.user import AppUser
from .store_serializers import StoreSerializer

class UserSerializer(serializers.ModelSerializer):
    """User Serializer class"""

    stores = StoreSerializer(many=True, required=False)

    def create_user(self, email, password, **kwargs):
        """Creates a normal user"""
        return AppUser.objects.create_user(email, password, **kwargs)

    class Meta:
        model = AppUser
        fields = ('__all__')


class UserContactSerializer():
    class Meta:
        Model = AppUser
        fields = ('city', 'state', 'address', 'phone_no', 'whatsapp_no', 'about',  'facebook', 'twitter',  )