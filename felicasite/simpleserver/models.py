from django.db import models
from django.contrib import admin
try:
    import json
except ImportError:
    import simplejson as json


class Card(models.Model):
    card_id = models.CharField(max_length=16)

    def __unicode__(self):
        return self.card_id

    @classmethod
    def load_json(cls, json_data):
        json_obj = json.loads(json_data)
        card_id = json_obj['card_id']
        cards = Card.objects.filter(card_id=card_id)
        if cards:
            card = cards[0]
        else:
            card = Card()

        for key, value in json_obj.items():
            setattr(card, key, value)

        return card


admin.site.register(Card)

