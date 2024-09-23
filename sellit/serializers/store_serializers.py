from sellit.serializers.item_serializers import ItemSerializer
from ..models.store import Store
from rest_framework import serializers

class StoreSerializer(serializers.ModelSerializer):
    """store serializer"""
    items = ItemSerializer(many=True, read_only=True)
    # owner = serializers.IntegerField(read_only=True)

    class Meta:
        model = Store
        fields = ('__all__')