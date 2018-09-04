"""
URL shortener.

Supported schemes: http, https.
"""
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import redirect
import random
import re
import requests
from urllib import parse
from django.core.cache import caches

if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
    )
    settings.CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': 'default_cache',
        },
        'counter_cache': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': 'counter_cache',
        }
    }
    urls_cache = caches['default']
    counter_cache = caches['counter_cache']


def random_key():
    key = ''.join([random.choice('123456789qwertyuiopasdfghjklzxc'
                                 'vbnmQWERTYUIOPASDFGHJKLZXCVBNM') for x in range(5)])
    print(key)
    return key


def index(request):
    return HttpResponse(__doc__)


def shorten(request, url):
    if re.match('(?i)https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url):
        request_test = requests.get(url, allow_redirects=False)
        rand_key = random_key()
        urls_cache.get_or_set(rand_key, url)
        counter_cache.set(rand_key, 0)
        return HttpResponse('<a href="http://localhost:8000/{0}">{0}</a>'.format(rand_key))
    else:
        return redirect('/')


def redirect_view(request, key):
    try:
        url_big = parse.urlparse(key)
        key = url_big.path
    except Exception:
        return redirect('/')
    if key in urls_cache:
        counter_cache.set(key, counter_cache.get(key) + 1)
        return redirect(urls_cache.get(key))
    else:
        return redirect('/')


def urlstats(request, key):
    if key in counter_cache:
        return HttpResponse('<h1>{0}</h1>'.format(counter_cache.get(key)))
    else:
        return redirect('/')


urlpatterns = [
    url(r'^$', index),
    # http://localhost:8000/shorten/<url>
    url(r'shorten/(.+)', shorten),
    # http://localhost:8000/urlstats/<key>
    url(r'urlstats/([\w\d]+)', urlstats),
    # http://localhost:8000/<key>
    url(r'([\w\d]+)', redirect_view),
]

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)