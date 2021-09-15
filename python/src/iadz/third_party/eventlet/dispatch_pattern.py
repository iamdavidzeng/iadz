import eventlet
from eventlet.green.urllib import request

pool = eventlet.GreenPool()


def fetch(url):
    return request.urlopen(url).read()


def app(environ, start_response):
    if environ["REQUEST_METHOD"] != "POST":
        start_response("403 Forbidden", [])
        return []

    pile = eventlet.GreenPile(pool)
    for line in environ["wsgi.input"].readlines():
        print(line)
        url = line.strip()
        if url:
            pile.spawn(fetch, url)

    titles = "\n".join(pile)
    start_response("200 OK", [{"Content-Type", "text/plain"}])
    return [titles]


if __name__ == "__main__":
    from eventlet import wsgi

    wsgi.server(eventlet.listen(("localhost", 9010)), app)
