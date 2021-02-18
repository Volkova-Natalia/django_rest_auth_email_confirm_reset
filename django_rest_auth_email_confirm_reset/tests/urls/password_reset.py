from . import BaseUrlsTestCase


class PasswordResetUrlsTestCase(BaseUrlsTestCase):
    end_point_name = 'password_reset'
    view_unit_name = 'password_reset'
    class_name = 'PasswordResetView'
    path = 'password-reset/'

    assert_message = end_point_name + ' urls'

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # ======================================================================

    def test_url(self):
        self.base_test_url(assert_message=self.assert_message)

    def test_view(self):
        self.base_test_view(assert_message=self.assert_message)

    def test_func(self):
        self.base_test_func(assert_message=self.assert_message)

    # ======================================================================
