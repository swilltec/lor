from django.db import models
from django.contrib.auth.models import AbstractUser

from simple_history.models import HistoricalRecords


class CustomUser(AbstractUser):
    """LoR Custom user model"""
    history = HistoricalRecords()

    def __str__(self):
        return self.username
