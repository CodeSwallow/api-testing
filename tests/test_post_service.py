import unittest
from unittest.mock import Mock, patch
from services import post_service

POSTS = [
    {"id": 1255, "user_id": 2525, "title": "Post title.", "body": "Post Body."},
    {"id": 1522, "user_id": 2520, "title": "Post title 2", "body": "Post Body 2"}
]
PK = 100  # for testing real API, could return 404


class TestRealPostAPIMatch(unittest.TestCase):
    """
        Test calls to real API, useful for comparing response keys to mock keys
    """

    @classmethod
    def setUpClass(cls):
        cls.api = post_service.PostService()

    def test_real_api_keys_match(self):
        resp = self.api.get_list()
        self.assertEqual(resp.status_code, 200)
        actual_keys = resp.json().pop().keys()

        with patch('services.post_service.PostService.get_list') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [{
                'id': 1,
                'user_id': 1555,
                'title': 'Post title',
                'body': 'Post body'
            }]

            mocked = self.api.get_list()
            mocked_keys = mocked.json().pop().keys()

        self.assertListEqual(list(actual_keys), list(mocked_keys))

    def test_can_reach_api(self):
        resp = self.api.get_list()
        self.assertEqual(resp.status_code, 200)
        resp = self.api.get_detail(pk=PK)
        self.assertTrue(resp.status_code == 200 or resp.status_code == 404)


class TestPostService(unittest.TestCase):
    """
        Mock tests for TodoService
    """

    @classmethod
    def setUpClass(cls):
        cls.api = post_service.PostService()

    def test_get_todos_list_ok(self):
        mock_get_patcher = patch('services.post_service.PostService.get_list')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = POSTS
        response = self.api.get_list()

        self.assertTrue(response.ok)
        self.assertListEqual(response.json(), POSTS)
        mock_get_patcher.stop()

    def test_get_todo_detail_ok(self):
        mock_get_patcher = patch('services.post_service.PostService.get_detail')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = POSTS[0]
        response = self.api.get_detail(pk=1557)

        self.assertTrue(response.ok)
        self.assertDictEqual(response.json(), POSTS[0])
        mock_get_patcher.stop()

    def test_get_comments_from_post_ok(self):
        mock_get_patcher = patch('services.post_service.PostService.get_comments')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True
        comments = [
            {"id": 1528, "post_id": 1536, "name": "Bankimchandra Bharadwaj", "email": "bharadwaj_bankimchandra@morar.org",
             "body": "Ut possimus ut. Quibusdam sed aut."},
            {"id": 1527, "post_id": 1536, "name": "Aruna Asan", "email": "aruna_asan@welch.net",
             "body": "Distinctio ab consequuntur. Ut necessitatibus molestiae."}
        ]

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = comments
        response = self.api.get_comments()

        self.assertTrue(response.ok)
        self.assertEqual(response.json(), comments)
        mock_get_patcher.stop()

    def test_post_comments_for_post_ok(self):
        mock_post_patcher = patch('services.post_service.PostService.post_comments')
        mock_post = mock_post_patcher.start()
        mock_post.return_value.ok = True
        comment = {"id": 1527, "post_id": 1536, "name": "Aruna Asan", "email": "aruna_asan@welch.net",
             "body": "Distinctio ab consequuntur. Ut necessitatibus molestiae."}

        mock_post.return_value = Mock()
        mock_post.return_value.json.return_value = comment
        response = self.api.post_comments(comment)

        self.assertTrue(response.ok)
        self.assertEqual(response.json(), comment)
        mock_post_patcher.stop()


if __name__ == '__main__':
    unittest.main()
