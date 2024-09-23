from django.db import models

from sellit.models import SellitBaseManager

from .store import Store
from .user import AppUser
# from sellit.models import SellitBaseManager


class Promotion(models.Model):
    """User promotions"""
    title = models.CharField(max_length=200)
    about = models.TextField()
    promoter = models.ForeignKey(AppUser, related_name="promotions", on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name="promotions", on_delete=models.CASCADE, blank=True, null=True)
    image_url = models.CharField(max_length=512,blank=True)
    phone_no = models.CharField(max_length=20,blank=True)
    whatsapp_no = models.CharField(max_length=15,blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    twitter = models.CharField(max_length=100,blank=True)
    website = models.CharField(max_length=512,blank=True)

    objects = SellitBaseManager()
