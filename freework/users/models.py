from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """Default user for freework."""

    first_name = None
    last_name = None

    name = models.CharField(_("name"), max_length=255, blank=True)
    email = models.EmailField(_("email"), unique=True)

    objects = UserManager()

    def __str__(self):
        return self.username
