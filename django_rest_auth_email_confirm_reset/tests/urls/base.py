from django.test import TestCase
from ...utils import ClassWithAbstractVariables
from django.urls import reverse, resolve

from ...settings import app_name
from ...utils import get_namespace, get_base_url


# Create your tests here.
class BaseUrlsTestCase(TestCase,
                       ClassWithAbstractVariables):
    base_url_expected = get_base_url()

    url_args = []

    # ======================================================================

    __required_class_variables = [
        "end_point_name",   # example:   end_point_name = 'auth_info'
        "view_unit_name",   # example:   view_unit_name = 'auth_info'
        "class_name",       # example:   class_name = 'AuthInfoView'
        "path",             # without base url, with '/' at the end (if it is necessary)
                            # example:   path = 'auth-info/'
    ]

    @classmethod
    def __init_subclass__(cls):
        super().__thisclass__.check_required_class_variables(child=cls)
        super().__init_subclass__()

    # ======================================================================

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        namespace = get_namespace()

        self.url_expected = self.base_url_expected + self.path
        self.view_expected = namespace + self.end_point_name
        self.func_expected = \
            app_name + '.' + 'views.' + self.view_unit_name + '.' + self.class_name

        self.url = reverse(namespace + self.end_point_name, args=self.url_args)
        self.view = resolve(self.url).view_name
        self.func = resolve(self.url)._func_path

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        super().setUp()
        # print('')
        # print('url_expected  ', self.url_expected)
        # print('url           ', self.url)
        # print('view_expected ', self.view_expected)
        # print('view          ', self.view)
        # print('func_expected ', self.func_expected)
        # print('func          ', self.func)

    def tearDown(self):
        super().tearDown()

    # ======================================================================

    def base_test_url(self, *, assert_message=''):
        # print('\nurl_expected  ', self.url_expected)
        # print('url           ', self.url)
        self.assertEquals(self.url, self.url_expected, assert_message + ' test url')
        pass

    def base_test_view(self, *, assert_message=''):
        # print('\nview_expected ', self.view_expected)
        # print('view          ', self.view)
        self.assertEquals(self.view, self.view_expected, assert_message + ' test view')
        pass

    def base_test_func(self, *, assert_message=''):
        # print('\nfunc_expected ', self.func_expected)
        # print('func          ', self.func)
        self.assertEquals(self.func, self.func_expected, assert_message + ' test func')
        pass

    # ======================================================================
