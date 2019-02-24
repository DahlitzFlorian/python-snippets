import gevent.monkey

from urllib.request import urlopen
from urllib.error import URLError


gevent.monkey.patch_all()
urls = ["http://www.google.com", "http://www.yandex.ru", "http://www.python.org"]


def print_head(url):
    print("Starting {}".format(url))
    try:
        data = urlopen(url).read()
    except URLError:
        data = "None"
    finally:
        print("{}: {} bytes: {}".format(url, len(data), data))


jobs = [gevent.spawn(print_head, _url) for _url in urls]

gevent.wait(jobs)
