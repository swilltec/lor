from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """LoR Custom user model"""

    def __str__(self):
        return self.username

