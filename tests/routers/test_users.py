from tests.base_test import BaseTest
from tests.factories.user_factory import UserFactory


class TestUsersRouter(BaseTest):
    def test_list(self):
        users = [UserFactory(), UserFactory()]
        self.session.commit()
        response = self.client.get(url="/api/users")

        expected_results = [{"username": user.username} for user in users]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_results)
