from ..settings import app_name
from django.urls import get_resolver


def get_base_app_name():
    base_app_name = ""
    for url_pattern in get_resolver().url_patterns:
        try:
            if (url_pattern.urlconf_name.__name__ == get_resolver(app_name + '.urls').urlconf_name):
                base_app_name = url_pattern.app_name
                break
        except:
            pass
    return base_app_name
