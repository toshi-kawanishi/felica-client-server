from django.test import TestCase
from django.test.client import Client
from nose.plugins.attrib import attr
from nose.tools import *
try:
    import json
except ImportError:
    import simplejson as json

from felicasite.simpleserver.models import Card


class TestCard(TestCase):

    @attr('model')
    def test_load_json(self):
        json_data = {'card_id': '0000000000000000'}

        card = Card.load_json(json.dumps(json_data))

        eq_(card.card_id, '0000000000000000')


class TestCardController(TestCase):

    fixtures = ['card.yaml']

    @attr('view')
    def test_get_when_id_is_valid(self):
        response = self.client.get('/card/0000000000000000')
        eq_(response.status_code, 200)
        ok_('0000000000000000' in response.content)

    @attr('view')
    def test_get_when_id_is_not_valid(self):
        response = self.client.get('/card/0000000000000001')
        eq_(response.status_code, 404)

    @attr('view')
    def test_put(self):
        json_data = {'card_id': '0000000000000002'}
        response = self.client.put('/card/0000000000000002',
				   json.dumps(json_data),
				   'application/json')
        eq_(response.status_code, 200)
        ok_(Card.objects.get(card_id='0000000000000002'))

    @attr('view')
    def test_put_when_card_id_is_duplicate(self):
        json_data = {'card_id': '0000000000000003'}
        for n in range(2):
            response = self.client.put('/card/0000000000000003',
                       json.dumps(json_data),
                       'application/json')
        ok_(len(Card.objects.filter(card_id='0000000000000003')) == 1)
