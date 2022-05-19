# Python CLI App

Simple CLI App using Python for making requests to an API. <br>
API: https://gorest.co.in/

___
For methods POST, PUT, PATCH and DELETE you must generate an access token from the API and add it to a .env file, similar to the .env.sample file in this repository

.env
```dotenv
AUTHORIZATION='Bearer yourKeyHere'
```

# Index
1. [Requirements](#requirements)
2. [Getting Started](#getting-started)
3. [Running commands](#running-commands)
4. [Users Endpoints Example](#users-endpoints-example)
5. [Running Tests](#running-tests)
---

### Requirements:
```
python = "^3.10"
requests = "^2.27.1"
click = "^8.1.3"
python-decouple = "^3.6"
```
---
### Getting Started:
1. Create virtual environment
```
python -m virtualenv cli_venv
```
2. Activate virtual environment
   1. Windows
    ```
    cli_venv\Scripts\activate
    ```
   2. Linux
   ```
   source cli_venv/bin/activate
   ```
3. Clone repository and cd to api-testing
```
cd api-testing
```
4. Install Requirements
```
pip install -r requirements.txt
```
---
### Running commands:
Running 'python main.py', will display the possible options and args that can be used
```shell
python main.py
```
```
Usage: main.py [OPTIONS] COMMAND [ARGS]...

  CLI app for making calls to endpoints at https://gorest.co.in/

Options:
  --help  Show this message and exit.

Commands:
  comments  Endpoint: '/comments'
  posts     Endpoint: '/posts'
  todos     Endpoint: '/todos'
  users     Endpoint: '/users'

```

#### Users Endpoints Example
```shell
python main.py users
```
```
Usage: main.py users [OPTIONS] COMMAND [ARGS]...

  Endpoint: '/users'

Options:
  --help  Show this message and exit.

Commands:
  create-post  Create post for existing user by passing its id and...
  create-todo  Create todo for existing user by passing its id and...
  delete       Delete existing user by passing its id (PRIMARY_KEY)
  get-detail   Call users api to retrieve user detail with id...
  get-list     Call users api to retrieve list of users with optional...
  get-posts    View posts of existing user by passing its id (PRIMARY_KEY)
  get-todos    View todos of existing user by passing its id (PRIMARY_KEY)
  patch        Partially modify existing user by passing its id...
  post         Create a new user
  put          Modify existing user by passing its id (PRIMARY_KEY)
```
#### Getting User Detail with Primary Key
```shell
pytho main.py users get-detail 2488
```
```
User details...
{'id': 2488, 'name': 'Gitanjali Joshi', 'email': 'joshi_gitanjali@hayes.net', 'gender': 'female', 'status': 'active'}
```
---
### Running Tests
Tests were written using the standard unittest library <br>
To run all test:
```
python -m unittest discover -s tests   
```

The test mostly use the Mock class and patch() function from the unittest.mock library <br>
To try to ensure that the mock requests represented real data from the actual API, tests that made calls to the real API were written to compare the keys returned to the keys used in the mock tests. <br>
##### To test individual an individual service:
```
python -m unittest tests.test_post_service
```
Test files: <br>
1. test_comment_service.py
2. test_post_service.py
3. test_todo_service.py
4. test_user_service.py