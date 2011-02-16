from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from felicasite.simpleserver.models import Card


def card(request, card_id):
    if request.method == 'GET':
        card = get_object_or_404(Card, card_id=card_id)
        return render_to_response('card.html',
                                  {'card_id': card.card_id})
    elif request.method == 'PUT':
        length_str = request.environ.get('CONTENT_LENGTH', 0)
        if length_str:
            length = int(length_str)
        else:
            length = 0

        stream = request.environ['wsgi.input']
        data = stream.read(length)

        card = Card.load_json(data)
        card.save()
        return HttpResponse(card_id)
