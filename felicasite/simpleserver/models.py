from django.db import models
from django.contrib import admin


class Card(models.Model):
    card_id = models.CharField(max_length=16)

    def __unicode__(self):
        return self.card_id


admin.site.register(Card)

