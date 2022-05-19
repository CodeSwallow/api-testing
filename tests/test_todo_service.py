import unittest
from unittest.mock import Mock, patch
from services import todo_service

TODOS = [
    {"id": 1557, "user_id": 3101, "title": "Desidero vae spiritus via territo ratione.",
     "due_on": "2022-06-11T00:00:00.000+05:30", "status": "pending"},
    {"id": 1556, "user_id": 3100, "title": "Vito velit corrigo vulgaris demoror aequus.",
     "due_on": "2022-05-29T00:00:00.000+05:30", "status": "pending"},
    {"id": 1552, "user_id": 3094, "title": "Eum amiculum vulnus blandior appositus.",
     "due_on": "2022-06-09T00:00:00.000+05:30", "status": "completed"}
]
PK = 100  # for testing real API, could return 404


class TestRealTodoAPIMatch(unittest.TestCase):
    """
        Test calls to real API, useful for comparing response keys to mock keys
    """

    @classmethod
    def setUpClass(cls):
        cls.api = todo_service.TodoService()

    def test_real_api_keys_match(self):
        resp = self.api.get_list()
        self.assertEqual(resp.status_code, 200)
        actual_keys = resp.json().pop().keys()

        with patch('services.todo_service.TodoService.get_list') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [{
                'id': 1,
                'user_id': 1,
                'title': 'Todo title',
                'due_on': '2022-05-29T00:00:00.000+05:30',
                'status': 'completed'
            }]

            mocked = self.api.get_list()
            mocked_keys = mocked.json().pop().keys()

        self.assertListEqual(list(actual_keys), list(mocked_keys))

    def test_can_reach_api(self):
        resp = self.api.get_list()
        self.assertEqual(resp.status_code, 200)
        resp = self.api.get_detail(pk=PK)
        self.assertTrue(resp.status_code == 200 or resp.status_code == 404)


class TestTodoService(unittest.TestCase):
    """
        Mock tests for TodoService
    """

    @classmethod
    def setUpClass(cls):
        cls.api = todo_service.TodoService()

    def test_get_todos_list_ok(self):
        mock_get_patcher = patch('services.todo_service.TodoService.get_list')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = TODOS
        response = self.api.get_list()

        self.assertTrue(response.ok)
        self.assertListEqual(response.json(), TODOS)
        mock_get_patcher.stop()

    def test_get_todo_detail_ok(self):
        mock_get_patcher = patch('services.todo_service.TodoService.get_detail')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = TODOS[0]
        response = self.api.get_detail(pk=1557)

        self.assertTrue(response.ok)
        self.assertDictEqual(response.json(), TODOS[0])
        mock_get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
