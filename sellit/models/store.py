from django.db import models
from .user import AppUser
from sellit.models import SellitBaseManager


class Store(models.Model):
    """User store"""
    owner = models.ForeignKey(AppUser, related_name="stores", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField()

    objects = SellitBaseManager()