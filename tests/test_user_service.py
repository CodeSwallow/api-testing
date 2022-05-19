import unittest
from unittest.mock import Mock, patch
from services import user_service

USERS = [
    {"id": 3385, "name": "John Smith", "email": "john@gmail.com", "gender": "male", "status": "active"},
    {"id": 3103, "name": "Shashi Gupta", "email": "gupta_shashi@bechtelar.biz", "gender": "male",
     "status": "inactive"},
    {"id": 3102, "name": "Bala Pilla VM", "email": "vm_pilla_bala@pouros.net", "gender": "female",
     "status": "inactive"},
]
PK_1 = 2525  # for testing real API, might return empty string and fail test_real_get_posts_api_keys_match
PK_2 = 2500  # for testing real API, might return empty string and fail test_real_get_todos_api_keys_match


class TestRealUserAPIMatch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = user_service.UserService()

    def test_real_api_keys_match(self):
        resp = self.api.get_list()
        self.assertEqual(resp.status_code, 200)
        actual_keys = resp.json().pop().keys()

        with patch('services.user_service.UserService.get_list') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [{
                'id': 1,
                'name': 'John Doe',
                'email': 'fake@gmail.com',
                'gender': 'Female',
                'status': 'active'
            }]

            mocked = self.api.get_list()
            mocked_keys = mocked.json().pop().keys()

        self.assertListEqual(list(actual_keys), list(mocked_keys))

    def test_can_reach_api(self):
        resp = self.api.get_list()
        self.assertEqual(resp.status_code, 200)
        resp = self.api.get_detail(pk=PK_1)
        self.assertTrue(resp.status_code == 200 or resp.status_code == 404)

    def test_real_get_todos_api_keys_match(self):
        resp = self.api.get_todos(pk=PK_2)
        self.assertEqual(resp.status_code, 200)
        actual_keys = resp.json().pop().keys()

        with patch('services.user_service.UserService.get_todos') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [{
                'id': 1,
                'user_id': 1,
                'title': 'Todo title',
                'due_on': '2022-05-29T00:00:00.000+05:30',
                'status': 'completed'
            }]

            mocked = self.api.get_todos()
            mocked_keys = mocked.json().pop().keys()

        self.assertListEqual(list(actual_keys), list(mocked_keys))

    def test_real_get_posts_api_keys_match(self):
        resp = self.api.get_posts(pk=PK_1)
        self.assertEqual(resp.status_code, 200)
        actual_keys = resp.json().pop().keys()

        with patch('services.user_service.UserService.get_posts') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [{
                'id': 1,
                'user_id': 1,
                'title': 'Post title',
                'body': 'Post body',
            }]

            mocked = self.api.get_posts()
            mocked_keys = mocked.json().pop().keys()

        self.assertListEqual(list(actual_keys), list(mocked_keys))


class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = user_service.UserService()

    def test_get_users_list_ok(self):
        mock_get_patcher = patch('services.user_service.UserService.get_list')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = USERS
        response = self.api.get_list()

        self.assertTrue(response.ok)
        self.assertListEqual(response.json(), USERS)
        mock_get_patcher.stop()

    def test_get_user_detail_ok(self):
        mock_get_patcher = patch('services.user_service.UserService.get_detail')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = USERS[0]
        response = self.api.get_detail(pk=3385)

        self.assertTrue(response.ok)
        self.assertDictEqual(response.json(), USERS[0])
        mock_get_patcher.stop()

    def test_post_user_ok(self):
        mock_post_patcher = patch('services.user_service.UserService.post')
        mock_post = mock_post_patcher.start()
        mock_post.return_value.ok = True

        mock_post.return_value = Mock()
        mock_post.return_value.json.return_value = USERS[0]
        response = self.api.post(USERS[0])

        self.assertTrue(response.ok)
        self.assertDictEqual(response.json(), USERS[0])
        mock_post_patcher.stop()

    def test_put_user_ok(self):
        mock_put_patcher = patch('services.user_service.UserService.put')
        mock_put = mock_put_patcher.start()
        mock_put.return_value.ok = True

        mock_put.return_value = Mock()
        mock_put.return_value.json.return_value = USERS[0]
        response = self.api.put(pk=3103)

        self.assertTrue(response.ok)
        self.assertDictEqual(response.json(), USERS[0])
        mock_put_patcher.stop()

    def test_patch_user_ok(self):
        mock_patch_patcher = patch('services.user_service.UserService.patch')
        mock_patch = mock_patch_patcher.start()
        mock_patch.return_value.ok = True

        mock_patch.return_value = Mock()
        mock_patch.return_value.json.return_value = USERS[0]
        response = self.api.patch(USERS[0]['name'], pk=3103)

        self.assertTrue(response.ok)
        self.assertDictEqual(response.json(), USERS[0])
        mock_patch_patcher.stop()

    def test_delete_user_ok(self):
        mock_delete_patcher = patch('services.user_service.UserService.delete')
        mock_delete = mock_delete_patcher.start()
        mock_delete.return_value.ok = True

        mock_delete.return_value = Mock()
        mock_delete.return_value.json.return_value = []
        response = self.api.delete(pk=3103)

        self.assertTrue(response.ok)
        self.assertEqual(response.json(), [])
        mock_delete_patcher.stop()

    def test_user_get_posts_ok(self):
        mock_get_patcher = patch('services.user_service.UserService.get_posts')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True
        posts = [{"id": 2, "user_id": 3010, "title": "Todo Title", "body": "Todo Body"}]

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = posts
        response = self.api.get_posts()

        self.assertTrue(response.ok)
        self.assertEqual(response.json(), posts)
        mock_get_patcher.stop()

    def test_user_create_posts_ok(self):
        mock_post_patcher = patch('services.user_service.UserService.post_posts')
        mock_post = mock_post_patcher.start()
        mock_post.return_value.ok = True
        todo = {"id": 2, "user_id": 3010, "title": "Todo Title", "body": "Todo Body"}

        mock_post.return_value = Mock()
        mock_post.return_value.json.return_value = todo
        response = self.api.post_posts(todo)

        self.assertTrue(response.ok)
        self.assertEqual(response.json(), todo)
        mock_post_patcher.stop()

    def test_user_get_todos_ok(self):
        mock_get_patcher = patch('services.user_service.UserService.get_todos')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.ok = True
        todos = [{"id": 2, "user_id": 3010, "title": "Todo Title", "due_on": "2022-05-29T00:00:00.000+05:30",
                 "status": "completed"}]

        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = todos
        response = self.api.get_todos()

        self.assertTrue(response.ok)
        self.assertEqual(response.json(), todos)
        mock_get_patcher.stop()

    def test_user_create_todo_ok(self):
        mock_post_patcher = patch('services.user_service.UserService.post_todos')
        mock_post = mock_post_patcher.start()
        mock_post.return_value.ok = True
        todo = {"id": 2, "user_id": 3010, "title": "Todo Title", "due_on": "2022-05-29T00:00:00.000+05:30", "status": "completed"}

        mock_post.return_value = Mock()
        mock_post.return_value.json.return_value = todo
        response = self.api.post_todos(todo)

        self.assertTrue(response.ok)
        self.assertEqual(response.json(), todo)
        mock_post_patcher.stop()


if __name__ == '__main__':
    unittest.main()
