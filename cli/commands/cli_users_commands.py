import click
from cli.utilities.utilities import CheckInputs
from services.user_service import UserService


@click.command()
@click.option('--page', default=1, help='page number of user list')
@click.option('--name', default=None, help='filter by name')
@click.option('--email', default=None, help='filter by email')
@click.option('--gender', default=None, help='filter by gender')
@click.option('--status', default=None, help='filter by status')
def get_list(page, name, email, gender, status):
    """
        Call users api to retrieve list of users with optional query params
    """
    filters = {'page': page}
    if name is not None:
        filters['name'] = name
    if email is not None:
        filters['email'] = email
    if gender is not None:
        filters['gender'] = gender
    if status is not None:
        filters['status'] = status
    click.echo("Getting users...")
    api = UserService()
    resp = api.get_list(query_params=filters)
    if resp.status_code == 200:
        if len(resp.json()) == 0:
            click.echo('Empty')
        for user in resp.json():
            click.echo(user)
    else:
        click.echo(f"Could not reach server: {resp.status_code}")


@click.command()
@click.argument('primary_key')
def get_detail(primary_key):
    """
        Call users api to retrieve user detail with id (PRIMARY_KEY) given
    """
    click.echo("User details...")
    try:
        pk = int(primary_key)
        api = UserService()
        resp = api.get_detail(pk=pk)
        if resp.status_code == 200:
            click.echo(resp.json())
        elif resp.status_code == 404:
            click.echo(f"Could not find user with id: {primary_key}")
        else:
            click.echo(f"Error: {resp.status_code}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")


@click.command()
@click.argument('name')
@click.argument('email')
@click.argument('gender', type=click.Choice(['male', 'female']))
@click.argument('status', type=click.Choice(['active', 'inactive']))
def post(name, email, gender, status):
    """
        Create a new user
    """
    api = UserService()
    click.echo("Creating user...")
    new_user = {'name': name, 'gender': gender, 'status': status}
    if not CheckInputs.check_email(email):
        click.echo('Invalid mail')
        return
    new_user['email'] = email
    resp = api.post(new_user)
    if resp.status_code == 201:
        click.echo(f"User created: {resp.json()}")
    else:
        click.echo(f"Error: {resp.status_code}, {resp.json()}")


@click.command()
@click.argument('primary_key')
@click.argument('name')
@click.argument('email')
@click.argument('gender', type=click.Choice(['male', 'female']))
@click.argument('status', type=click.Choice(['active', 'inactive']))
def put(primary_key, name, email, gender, status):
    """
        Modify existing user by passing its id (PRIMARY_KEY)
    """
    click.echo("Modifying user...")
    try:
        pk = int(primary_key)
        api = UserService()
        updated_user = {'name': name, 'gender': gender, 'status': status}
        if not CheckInputs.check_email(email):
            click.echo('Invalid mail')
            return
        updated_user['email'] = email
        resp = api.put(updated_user, pk=pk)
        if resp.status_code == 200:
            click.echo(f"User modified: {resp.json()}")
        else:
            click.echo(f"Error: {resp.status_code}, {resp.json()}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")


@click.command()
@click.argument('primary_key')
@click.option('--name', default=None, help='modify name')
@click.option('--email', default=None, help='modify email')
@click.option('--gender', default=None, help='modify gender')
@click.option('--status', default=None, help='modify status')
def patch(primary_key, name, email, gender, status):
    """
        Partially modify existing user by passing its id (PRIMARY_KEY)
    """
    click.echo("Partially modifying user...")
    try:
        pk = int(primary_key)
        api = UserService()
        updated_user = {}
        if name is not None:
            updated_user['name'] = name
        if email is not None:
            if not CheckInputs.check_email(email):
                click.echo('Invalid mail')
            else:
                updated_user['email'] = email
        if gender is not None:
            updated_user['gender'] = gender
        if status is not None:
            updated_user['status'] = status
        resp = api.put(updated_user, pk=pk)
        if resp.status_code == 200:
            click.echo(f"User modified: {resp.json()}")
        else:
            click.echo(f"Error: {resp.status_code}, {resp.json()}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")


@click.command()
@click.argument('primary_key')
def delete(primary_key):
    """
        Delete existing user by passing its id (PRIMARY_KEY)
    """
    click.echo("Deleting user...")
    try:
        pk = int(primary_key)
        api = UserService()
        resp = api.delete(pk=pk)
        if resp.status_code == 204:
            click.echo("User deleted")
        else:
            click.echo(f"Error: {resp.status_code}, {resp.json()}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")


@click.command()
@click.argument('primary_key')
def get_todos(primary_key):
    """
        View todos of existing user by passing its id (PRIMARY_KEY)
    """
    click.echo("Getting user's todos...")
    try:
        pk = int(primary_key)
        api = UserService()
        resp = api.get_todos(pk=pk)
        if resp.status_code == 200:
            if len(resp.json()) == 0:
                click.echo('Empty')
            for todo in resp.json():
                click.echo(todo)
        else:
            click.echo(f"Error: {resp.status_code}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")


@click.command()
@click.argument('primary_key')
@click.argument('title')
@click.argument('due_on', type=click.DateTime())
@click.argument('status', type=click.Choice(['pending', 'completed']))
def create_todo(primary_key, title, due_on, status):
    """
        Create todo for existing user by passing its id and required arguments for new todo
    """
    click.echo("Creating todo for user...")
    try:
        pk = int(primary_key)
        api = UserService()
        new_todo = {'title': title, 'due_on': due_on, 'status': status}
        resp = api.post_todos(new_todo, pk=pk)
        if resp.status_code == 201:
            click.echo(f"Todo created: {resp.json()}")
        else:
            click.echo(f"Error: {resp.status_code}, {resp.json()}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")


@click.command()
@click.argument('primary_key')
def get_posts(primary_key):
    """
        View posts of existing user by passing its id (PRIMARY_KEY)
    """
    click.echo("Getting user's posts...")
    try:
        pk = int(primary_key)
        api = UserService()
        resp = api.get_posts(pk=pk)
        if resp.status_code == 200:
            if len(resp.json()) == 0:
                click.echo('Empty')
            for post_item in resp.json():
                click.echo(post_item)
        else:
            click.echo(f"Error: {resp.status_code}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")


@click.command()
@click.argument('primary_key')
@click.argument('title')
@click.argument('body')
def create_post(primary_key, title, body):
    """
        Create post for existing user by passing its id and required arguments for new todo
    """
    click.echo("Creating post for user...")
    try:
        pk = int(primary_key)
        api = UserService()
        new_todo = {'title': title, 'body': body}
        resp = api.post_posts(new_todo, pk=pk)
        if resp.status_code == 201:
            click.echo(f"Post created: {resp.json()}")
        else:
            click.echo(f"Error: {resp.status_code}, {resp.json()}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")
