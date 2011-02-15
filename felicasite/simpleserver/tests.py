from django.test import TestCase
from django.test.client import Client
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


class TestCardController(TestCase):

    @attr('view')
    def test_get(self):
        response = self.client.get('/card/0000000000000000')
        eq_(response.status_code, 200)
        ok_('0000000000000000' in response.content)
