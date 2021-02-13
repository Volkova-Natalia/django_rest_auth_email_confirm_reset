from ..views.base import BaseRegistrationViewsTestCase


# Create your tests here.
class RegistrationIntegrationTestCase(BaseRegistrationViewsTestCase):

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
        self.data_expected['post'][success_fail] = self.user.copy()
        self.data_expected['post'][success_fail]['name'] = None
        self.data_expected['post'][success_fail]['last_login'] = None
        self.base_test_post(response=response, success_fail=success_fail, assert_message='integration')

        return client

    # ======================================================================

    def test(self):
        assert_message = 'integration registration'
        pass
        # TODO

    # ======================================================================
