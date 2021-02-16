from ..views.base import BaseConfirmationViewsTestCase


# Create your tests here.
class ConfirmationIntegrationTestCase(BaseConfirmationViewsTestCase):

    # ======================================================================

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    # ======================================================================

    def execute(self, *, client=None):
        success_fail = 'success'

        confirmation_link = self.get_confirmation_link()
        confirmation_args = self.get_confirmation_args(confirmation_link=confirmation_link)
        self.set_url(uidb64=confirmation_args['uidb64'], token=confirmation_args['token'])

        client, response = self.get(client=client)
        self.base_test_get(response=response, success_fail=success_fail, assert_message='integration')

        return client

    # ======================================================================

    def test(self):
        assert_message = 'integration confirmation'
        pass
        # TODO

    # ======================================================================
