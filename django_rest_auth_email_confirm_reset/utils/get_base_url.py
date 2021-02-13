from ..settings import end_point
from .get_namespace import get_namespace
from django.urls import reverse


def get_base_url():
    base_url = r'/'
    namespace = get_namespace()
    some_end_point = list(end_point.values())[0]
    absolute_url_some_end_point = reverse(namespace + some_end_point['name'])
    pos_local_url_some_end_point = absolute_url_some_end_point.find(some_end_point['url'])
    base_url = absolute_url_some_end_point[:pos_local_url_some_end_point]
    return base_url
