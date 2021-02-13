from django.views.generic import TemplateView

from ..settings import app_name
from ..utils import get_base_url


class SwaggerExpectedView(TemplateView):

    # --------------------------------------------------

    def __init__(self, **kwargs):
        base_url = get_base_url()

        kwargs['template_name'] = app_name + r'/swagger/index.html'
        kwargs['extra_context'] = {'base_url': base_url, 'app_name': app_name}

        super().__init__(**kwargs)
