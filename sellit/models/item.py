from django.db import models

from sellit.models import SellitBaseManager

from .store import Store


class Currency(models.TextChoices):
    NAIRA = "NG", "NAIRA"
    DOLLAR = "US", "DOLLAR"

class Item(models.Model):
    """Products in store"""
    name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, related_name="items", on_delete=models.CASCADE, null=False)
    currency = models.CharField(max_length=2, choices=Currency.choices, default=Currency.NAIRA)
    price = models.IntegerField(blank=True, null=True)
    desc = models.TextField()
    image_url = models.CharField(max_length=512, blank=True)
    # ads = models.ForeignKey(Promotion, related_name="promotions", on_delete=models.CASCADE, null=False)

    objects = SellitBaseManager()
    