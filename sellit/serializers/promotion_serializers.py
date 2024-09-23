from rest_framework import serializers
from ..models import Promotion

class PromotionSerializer(serializers.ModelSerializer):
    """User promotions"""

    class Meta:
        model = Promotion
        fields  = ('__all__')