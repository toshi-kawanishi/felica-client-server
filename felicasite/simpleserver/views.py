from django.shortcuts import render_to_response, get_object_or_404
from felicasite.simpleserver.models import Card

def card(request, card_id):
    #card = Card.objects.get(card_id=card_id)
    card = get_object_or_404(Card, card_id=card_id)
    return render_to_response('card.html',
                              {'card_id': card.card_id})
