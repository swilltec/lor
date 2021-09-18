from django.db import models
from django.contrib.auth.models import AbstractUser

from simple_history.models import HistoricalRecords


class CustomUser(AbstractUser):
    """LoR Custom user model"""
    history = HistoricalRecords()

    def __str__(self):
        return self.username


class Character(models.Model):
    """Character model"""
    item_id = models.CharField(max_length=30)
    height = models.CharField(max_length=10, null=True, blank=True)
    race = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    birth = models.CharField(max_length=10, null=True, blank=True)
    spouse = models.CharField(max_length=50, null=True, blank=True)
    death = models.CharField(max_length=100, null=True, blank=True)
    realm = models.CharField(max_length=100, null=True, blank=True)
    heir = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    wiki_url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    """Quote model"""
    item_id = models.CharField(max_length=30)
    dialog = models.TextField(null=True, blank=True)
    movie= models.CharField(max_length=30)
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.item_id

class Favorites(models.Model):
    """Favorited items model"""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quote = models.ForeignKey(
        Quote, on_delete=models.CASCADE, null=True, blank=True)
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()
