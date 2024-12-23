from tests.base_test import BaseTest


class TestUsersRouter(BaseTest):
    def test_list(self):
        response = self.client.get(url="/api/users")
        
        expected_results = [{"username": "Rick"}, {"username": "Morty"}]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_results)
        