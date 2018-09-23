from django.conf.urls import url
from django.conf import settings
from django.http import HttpResponse

settings.configure(
    ROOT_URLCONF = __name__,
    DEBUG = True
)

from pprint import pprint

# fort = """
# <form>

def index(request):
    out = ['{}:{}'.format(k, v)
           for k, v in sorted(request.META.items())
           if k.startwith('HTTP_')]
    html = '<br>'.join(out)
    html += '<br>Method: '