import unittest
from unittest.mock import Mock, patch
from services import comment_service

COMMENTS = [
    {"id": 1528, "post_id": 1536, "name": "Bankimchandra Bharadwaj", "email": "bharadwaj_bankimchandra@morar.org",
     "body": "Ut possimus ut. Quibusdam sed aut."},
    {"id": 1527, "post_id": 1536, "name": "Aruna Asan", "email": "aruna_asan@welch.net",
     "body": "Distinctio ab consequuntur. Ut necessitatibus molestiae."}
]
PK = 100  # for testing real API, could return 404


class TestRealCommentAPIMatch(unittest.TestCase):
    """
        Test calls to real API, useful for comparing response keys to mock keys
    """

    @classmethod
    def setUpClass(cls):
        cls.api = comment_service.CommentService()

    def test_real_api_keys_match(self):
        resp = self.api.get_list()
        self.assertEqual(resp.status_code, 200)
        actual_keys = resp.json().pop().keys()

        with patch('services.comment_service.CommentService.get_list') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [{
                'id': 1,
                'post_id': 1555,
                'name': 'Comment name',
                'email': "jain_sen_bhadra@pagac-tillman.biz",
                'body': 'Comment body'
            }]

            mocked = self.api.get_list()
            mocked_keys = mocked.json().pop().keys()

        self.assertListEqual(list(actual_keys), list(mocked_keys))

    def test_can_reach_api(self):
        resp = self.api.get_list()
        self.assertEqual(resp.status_code, 200)
        resp = self.api.get_detail(pk=PK)
        self.assertTrue(resp.status_code == 200 or resp.status_code == 404)


class TestCommentService(unittest.TestCase):
    """
        Mock tests for TodoService
    """

    @classmethod
    def setUpClass(cls):
        cls.api = comment_service.CommentService()

    def test_get_todos_list_ok(self):
        mock_get_patcher = patch('services.comment_service.CommentService.get_list')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = COMMENTS
        response = self.api.get_list()

        self.assertTrue(response.ok)
        self.assertListEqual(response.json(), COMMENTS)
        mock_get_patcher.stop()

    def test_get_todo_detail_ok(self):
        mock_get_patcher = patch('services.comment_service.CommentService.get_detail')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = COMMENTS[0]
        response = self.api.get_detail(pk=1557)

        self.assertTrue(response.ok)
        self.assertDictEqual(response.json(), COMMENTS[0])
        mock_get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
