from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.db import models
# from django.contrib.auth import models
from rest_framework import serializers
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from sellit.models import SellitBaseManager


class MyUserManager(UserManager):
    def _create_user(self, email, password, username, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        # if not username:
        #     raise ValueError("The given username must be set")
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, username="", **extra_fields):
        # extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, username, **extra_fields)

    def create_superuser(self, email, password, username="", **extra_fields):
        # extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # if extra_fields.get("is_staff") is not True:
        #     raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, username, password, **extra_fields)

class UserSubscription(models.TextChoices):
    FREE = "FF", "FREE"
    PAID = "PP", "PAID"

class AppUser(AbstractBaseUser):
    """App User"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    username = models.CharField(max_length=255, unique=True)

    ratings = models.IntegerField(default=0)

    city = models.CharField(max_length=255, blank=True)

    state = models.CharField(max_length=255, blank=True)

    address = models.CharField(max_length=255, blank=True)

    image_url = models.CharField(max_length=512, blank=True)

    about = models.TextField(blank=True)

    phone_no = models.CharField(max_length=20, blank=True)

    whatsapp_no = models.CharField(max_length=100, blank=True)
    phone_no = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)

    website = models.CharField(max_length=255, blank=True)

    email_verified = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False, help_text=_("Designate whether user can log on to admin site."))

    subscription = models.CharField(max_length=2, choices=UserSubscription.choices, default=UserSubscription.FREE)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'