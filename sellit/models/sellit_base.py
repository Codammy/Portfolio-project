#!/usr/bin/pythno3
""" Custom base model for sellit models"""
from django.db import models
from django.http import Http404, JsonResponse


class SellitBaseManager(models.Manager):
    def get_or_404(self, id):
        """
        bahaves like the object.get method except
        that it returns 404 Response if resource 
        queried doesn't exist instead of the normal DoesNotExist exception
        """

        try:
            return super().get(id=id)
        except Exception as e:
            raise Http404(e)



# class SellitBaseModel(models.Model):
#     """Sellit base model class"""

#     objects = SellitBaseManager()

