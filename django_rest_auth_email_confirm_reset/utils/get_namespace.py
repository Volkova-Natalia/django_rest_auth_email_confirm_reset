from ..settings import app_name
from django.urls import get_resolver


def get_namespace():
    namespace = ""
    for url_pattern in get_resolver().url_patterns:
        try:
            if (url_pattern.urlconf_name.__name__ == get_resolver(app_name + '.urls').urlconf_name):
                namespace = url_pattern.namespace + ":"
                break
        except:
            pass
    return namespace
