from . import BaseUrlsTestCase


class ConfirmationUrlsTestCase(BaseUrlsTestCase):
    end_point_name = 'confirmation'
    view_unit_name = 'confirmation'
    class_name = 'ConfirmationView'
    uidb64 = 'Ab'
    token = 'ab01cd-e2345678f90gh123456i7j8k9l0mno12'
    url_args = [uidb64, token]
    path = 'confirmation/' + uidb64 + '/' + token + '/'

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
