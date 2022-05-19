import click
from cli.utilities.utilities import CheckInputs
from services.post_service import PostService


@click.command()
@click.option('--page', default=1, help='page number of user list')
@click.option('--user_id', default=None, help='filter by post id')
@click.option('--title', default=None, help='filter by name')
@click.option('--body', default=None, help='filter by body text')
def get_list(page, user_id, title, body):
    """
        Call posts api to retrieve list of posts with optional query params
    """
    filters = {'page': page}
    if user_id is not None:
        filters['user_id'] = user_id
    if title is not None:
        filters['title'] = title
    if body is not None:
        filters['body'] = body
    click.echo("Getting posts...")
    api = PostService()
    resp = api.get_list(query_params=filters)
    if resp.status_code == 200:
        if len(resp.json()) == 0:
            click.echo('Empty')
        for post in resp.json():
            click.echo(post)
    else:
        click.echo(f"Error: {resp.status_code}")


@click.command()
@click.argument('primary_key')
def get_detail(primary_key):
    """
        Call posts api to retrieve post detail with id (PRIMARY_KEY) given
    """
    click.echo("Post details...")
    try:
        pk = int(primary_key)
        api = PostService()
        resp = api.get_detail(pk=pk)
        if resp.status_code == 200:
            click.echo(resp.json())
        elif resp.status_code == 404:
            click.echo(f"Could not find post with id: {primary_key}")
        else:
            click.echo(f"Error: {resp.status_code}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")


@click.command()
@click.argument('primary_key')
def get_comments(primary_key):
    """
        View comments of existing post by passing its id (PRIMARY_KEY)
    """
    click.echo("Getting post's comments...")
    try:
        pk = int(primary_key)
        api = PostService()
        resp = api.get_comments(pk=pk)
        if resp.status_code == 200:
            if len(resp.json()) == 0:
                click.echo('Empty')
            for comment in resp.json():
                click.echo(comment)
        else:
            click.echo(f"Error: {resp.status_code}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")


@click.command()
@click.argument('primary_key')
@click.argument('name')
@click.argument('email')
@click.argument('body')
def post_comments(primary_key, name, email, body):
    """
        Create comment for existing post by passing its id and required arguments for new comment
    """
    click.echo("Creating comment for post...")
    try:
        pk = int(primary_key)
        api = PostService()
        new_comment = {'name': name, 'body': body}
        if not CheckInputs.check_email(email):
            click.echo('Invalid mail')
            return
        new_comment['email'] = email
        resp = api.post_comments(new_comment, pk=pk)
        if resp.status_code == 201:
            click.echo(f"Comment created: {resp.json()}")
        else:
            click.echo(f"Error: {resp.status_code}, {resp.json()}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")
