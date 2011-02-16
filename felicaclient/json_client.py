try:
    import json
except ImportError:
    import simplejson as json
import simpleclient
import sys


def put_json(felica, uri):
    import httplib2
    http = httplib2.Http()
    headers = {'content-type': 'application/json'}
    try:
        card_id = felica.getidm()
        json_data = json.dumps({'card_id': card_id})
        response, content = http.request('%s/card/%s' % (uri, card_id), 'PUT',
                                         headers=headers, body=json_data)
        print "'%s, %s'" % (uri, json_data)
    except ValueError:
        pass


if __name__ == '__main__':
    server = simpleclient.SimpleFelicaClient()

    uri = sys.argv[1]
    server.run(put_json, args=(uri,), timeout=10)
