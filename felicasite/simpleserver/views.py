from django.shortcuts import render_to_response
from django.http import HttpResponse

def card(request, card_id):
    return render_to_response('card.html',
                              {'card_id': card_id})
