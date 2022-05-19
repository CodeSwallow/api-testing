import click
from services.comment_service import CommentService


@click.command()
@click.option('--page', default=1, help='page number of user list')
@click.option('--post_id', default=None, help='filter by post id')
@click.option('--name', default=None, help='filter by name')
@click.option('--email', default=None, help='filter by email')
@click.option('--body', default=None, help='filter by body text')
def get_list(page, post_id, name, email, body):
    """
        Call comments api to retrieve list of todos with optional query params
    """
    filters = {'page': page}
    if post_id is not None:
        filters['post_id'] = post_id
    if name is not None:
        filters['name'] = name
    if email is not None:
        filters['email'] = email
    if body is not None:
        filters['body'] = body
    click.echo("Getting comments...")
    api = CommentService()
    resp = api.get_list(query_params=filters)
    if resp.status_code == 200:
        if len(resp.json()) == 0:
            click.echo('Empty')
        for comment in resp.json():
            click.echo(comment)
    else:
        click.echo(f"Error: {resp.status_code}")


@click.command()
@click.argument('primary_key')
def get_detail(primary_key):
    """
        Call comments api to retrieve comment detail with id (PRIMARY_KEY) given
    """
    click.echo("Comment details...")
    try:
        pk = int(primary_key)
        api = CommentService()
        resp = api.get_detail(pk=pk)
        if resp.status_code == 200:
            click.echo(resp.json())
        elif resp.status_code == 404:
            click.echo(f"Could not find comment with id: {primary_key}")
        else:
            click.echo(f"Error: {resp.status_code}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")