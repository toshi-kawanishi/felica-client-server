from django.db import models
from django.contrib import admin
import json


class Card(models.Model):
    card_id = models.CharField(max_length=16)

    def __unicode__(self):
        return self.card_id

    def load_json(self, json_data):
        json_obj = json.loads(json_data)
        self.card_id = json_obj['card_id']


admin.site.register(Card)

