import re
import click
from services.user_service import UserService
from services.todo_service import TodoService
from services.post_service import PostService
from services.comment_service import CommentService
from cli.cli_groups import cli


# class CheckInputs:
#
#     @staticmethod
#     def check_email(email):
#         regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#         if re.fullmatch(regex, email):
#             return True
#         return False
#
#
# @click.group()
# def cli():
#     """
#         CLI app for making calls to endpoints at https://gorest.co.in/
#     """
#     pass
#
#
# @cli.group()
# def users():
#     """
#         CLI app for making calls to endpoints at https://gorest.co.in/
#         \nEndpoint: '/users'
#     """
#     pass
#
#
# @users.command()
# @click.option('--page', default=1, help='page number of user list')
# @click.option('--name', default=None, help='filter by name')
# @click.option('--email', default=None, help='filter by email')
# @click.option('--gender', default=None, help='filter by gender')
# @click.option('--status', default=None, help='filter by status')
# def get_list(page, name, email, gender, status):
#     """
#         Call users api to retrieve list of users with optional query params
#     """
#     filters = {'page': page}
#     if name is not None:
#         filters['name'] = name
#     if email is not None:
#         filters['email'] = email
#     if gender is not None:
#         filters['gender'] = gender
#     if status is not None:
#         filters['status'] = status
#     click.echo("Getting users...")
#     api = UserService()
#     resp = api.get_list(query_params=filters)
#     if resp.status_code == 200:
#         if len(resp.json()) == 0:
#             click.echo('Empty')
#         for user in resp.json():
#             click.echo(user)
#     else:
#         click.echo(f"Could not reach server: {resp.status_code}")
#
#
# @users.command()
# @click.argument('primary_key')
# def get_detail(primary_key):
#     """
#         Call users api to retrieve user detail with id (PRIMARY_KEY) given
#     """
#     click.echo("User details...")
#     try:
#         pk = int(primary_key)
#         api = UserService()
#         resp = api.get_detail(pk=pk)
#         if resp.status_code == 200:
#             click.echo(resp.json())
#         elif resp.status_code == 404:
#             click.echo(f"Could not find user with id: {primary_key}")
#         else:
#             click.echo(f"Error: {resp.status_code}")
#     except ValueError:
#         click.echo(f"Primary Key must be an integer")
#
#
# @users.command()
# @click.argument('name')
# @click.argument('email')
# @click.argument('gender', type=click.Choice(['male', 'female']))
# @click.argument('status', type=click.Choice(['active', 'inactive']))
# def post(name, email, gender, status):
#     """
#         Create a new user
#     """
#     api = UserService()
#     click.echo("Creating user...")
#     new_user = {'name': name, 'gender': gender, 'status': status}
#     if not CheckInputs.check_email(email):
#         click.echo('Invalid mail')
#         return
#     new_user['email'] = email
#     resp = api.post(new_user)
#     if resp.status_code == 201:
#         click.echo(f"User created: {resp.json()}")
#     else:
#         click.echo(f"Error: {resp.status_code}, {resp.json()}")
#
#
# @users.command()
# @click.argument('primary_key')
# @click.argument('name')
# @click.argument('email')
# @click.argument('gender', type=click.Choice(['male', 'female']))
# @click.argument('status', type=click.Choice(['active', 'inactive']))
# def put(primary_key, name, email, gender, status):
#     """
#         Modify existing user by passing its id (PRIMARY_KEY)
#     """
#     click.echo("Modifying user...")
#     try:
#         pk = int(primary_key)
#         api = UserService()
#         updated_user = {'name': name, 'gender': gender, 'status': status}
#         if not CheckInputs.check_email(email):
#             click.echo('Invalid mail')
#             return
#         updated_user['email'] = email
#         resp = api.put(updated_user, pk=pk)
#         if resp.status_code == 200:
#             click.echo(f"User modified: {resp.json()}")
#         else:
#             click.echo(f"Error: {resp.status_code}, {resp.json()}")
#     except ValueError:
#         click.echo(f"Primary Key must be an integer")
#
#
# @users.command()
# def patch():
#     """
#         Partially modify existing user by passing its id (PRIMARY_KEY)
#     """
#     click.echo("Partially modifying user...")
#
#
# @users.command()
# def delete():
#     """
#         Delete existing user by passing its id (PRIMARY_KEY)
#     """
#     click.echo("Deleting user...")
#
#
# @users.command()
# def get_todos():
#     """
#         View todos of existing user by passing its id (PRIMARY_KEY)
#     """
#     click.echo("Getting user's todos...")
#
#
# @users.command()
# def create_todo():
#     """
#         Create todo for existing user by passing its id and required arguments for new todo
#     """
#     click.echo("Creating todo for user...")
#
#
# @users.command()
# def get_posts():
#     """
#         View posts of existing user by passing its id (PRIMARY_KEY)
#     """
#     click.echo("Getting user's posts...")
#
#
# @users.command()
# def create_post():
#     """
#         Create post for existing user by passing its id and required arguments for new todo
#     """
#     click.echo("Creating post for user...")
#
#
# @cli.group()
# def todos():
#     """
#         CLI app for making calls to endpoints at https://gorest.co.in/
#         \nEndpoint: '/todos'
#     """
#     pass
#
#
# @todos.command()
# def get_list():
#     """
#         Call todos api to retrieve list of todos with optional query params
#     """
#     click.echo("Getting todos...")
#
#
# @todos.command()
# @click.argument('primary_key')
# def get_detail(primary_key):
#     """
#         Call todos api to retrieve todo detail with id (PRIMARY_KEY) given
#     """
#     click.echo("Getting todo details...")
#     try:
#         pk = int(primary_key)
#         api = TodoService()
#         resp = api.get_detail(pk=pk)
#         if resp.status_code == 200:
#             click.echo(resp.json())
#         elif resp.status_code == 404:
#             click.echo(f"Could not find todo with id: {primary_key}")
#         else:
#             click.echo(f"Error: {resp.status_code}")
#     except ValueError:
#         click.echo(f"Primary Key must be an integer")
#
#
# @cli.group()
# def posts():
#     """
#         CLI app for making calls to endpoints at https://gorest.co.in/
#         \nEndpoint: '/posts'
#     """
#     pass
#
#
# @posts.command()
# def get_list():
#     """
#         Call posts api to retrieve list of posts with optional query params
#     """
#     click.echo("Getting posts...")
#
#
# @posts.command()
# @click.argument('primary_key')
# def get_detail(primary_key):
#     """
#         Call posts api to retrieve post detail with id (PRIMARY_KEY) given
#     """
#     click.echo("Getting post's details...")
#     try:
#         pk = int(primary_key)
#         api = PostService()
#         resp = api.get_detail(pk=pk)
#         if resp.status_code == 200:
#             click.echo(resp.json())
#         elif resp.status_code == 404:
#             click.echo(f"Could not find post with id: {primary_key}")
#         else:
#             click.echo(f"Error: {resp.status_code}")
#     except ValueError:
#         click.echo(f"Primary Key must be an integer")
#
#
# @posts.command()
# def get_comments():
#     """
#         View comments of existing post by passing its id (PRIMARY_KEY)
#     """
#     click.echo("Getting post's comments...")
#
#
# @posts.command()
# def create_comment():
#     """
#         Create comment for existing post by passing its id and the required arguments for a new comment
#     """
#     click.echo("Creating comment for post...")
#
#
# @cli.group()
# def comments():
#     """
#         CLI app for making calls to endpoints at https://gorest.co.in/
#         \nEndpoint: '/comments'
#     """
#     pass
#
#
# @comments.command()
# def get_list():
#     """
#         Call comments api to retrieve list of comments with optional query params
#     """
#     click.echo("Getting comments...")
#
#
# @comments.command()
# @click.argument('primary_key')
# def get_detail(primary_key):
#     """
#         Call comments api to retrieve comment detail with id (PRIMARY_KEY) given
#     """
#     click.echo("Getting comment's details...")
#     try:
#         pk = int(primary_key)
#         api = CommentService()
#         resp = api.get_detail(pk=pk)
#         if resp.status_code == 200:
#             click.echo(resp.json())
#         elif resp.status_code == 404:
#             click.echo(f"Could not find comment with id: {primary_key}")
#         else:
#             click.echo(f"Error: {resp.status_code}")
#     except ValueError:
#         click.echo(f"Primary Key must be an integer")


if __name__ == '__main__':
    cli()
    # api = UserService()
    # resp = api.post({"name": "john doe", "email": "johultran@gmail.com", "gender": "male", "status": "active"})
    # print(resp.status_code, resp.json())
