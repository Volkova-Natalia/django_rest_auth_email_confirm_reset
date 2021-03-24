from ..views.base import BaseLoginViewsTestCase


# Create your tests here.
class LoginIntegrationTestCase(BaseLoginViewsTestCase):

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

        client, response = self.post(client=client)
        self.base_test_post(response=response, success_fail=success_fail, assert_message='integration')

        return client

    # ======================================================================

    def test(self):
        assert_message = 'integration login'
        pass
        # TODO

    # ======================================================================
