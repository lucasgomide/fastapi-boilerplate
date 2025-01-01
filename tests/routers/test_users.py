from tests.base_test import BaseRouterTest
from tests.factories.user_factory import UserFactory


class TestUsersRouter(BaseRouterTest):
    def test_list(self):
        users = [UserFactory(), UserFactory()]
        self.session.commit()
        response = self.client.get(url="/api/users")

        expected_items = [{"username": user.username} for user in users]
        
        self.assert_response_list(response=response, expected_items=expected_items)
        