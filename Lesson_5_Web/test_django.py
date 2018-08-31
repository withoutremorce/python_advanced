from django.conf.urls import url
from django.conf import settings
from django.http import HttpResponse
# print(django.get_version())

settings.configure(
    ROOT_URLCONF = __name__,
    DEBUG =True
)

def index(request):
    return HttpResponse('<h1>Hello, Django</h1>', content_type='text/html')

urpatterns = [
    url(r'', index)
]

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    import sys
    execute_from_command_line(sys.argv)
