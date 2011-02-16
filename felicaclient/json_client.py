try:
    import json
except ImportError:
    import simplejson as json
import simpleclient


def put_json(felica):
    json_data = json.dumps({'card_id': felica.getidm()})
    print "'%s'" % json_data


if __name__ == '__main__':
    server = simpleclient.SimpleFelicaClient()
    server.run(put_json, timeout=10)
