from django.db import models

class Card(models.Model):
    card_id = models.CharField(max_length=16)
