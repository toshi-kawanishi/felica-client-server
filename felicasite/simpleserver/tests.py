from django.test import TestCase
from nose.plugins.attrib import attr
from nose.tools import *
import json

from felicasite.simpleserver.models import Card


class TestCard(TestCase):

    @attr('model')
    def test_load_json(self):
        json_data = {'card_id': '0000000000000000'}
        card = Card()

        card.load_json(json.dumps(json_data))

        eq_(card.card_id, '0000000000000000')
