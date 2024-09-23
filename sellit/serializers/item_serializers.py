from rest_framework import serializers
from ..models import Item
# from .item_serializers import PromotionSerializer

class ItemSerializer(serializers.ModelSerializer):
    """Products in store"""
    # ads=PromotionSerializer(manyTrue=True)

    class Meta:
        model = Item
        fields = ('__all__')
