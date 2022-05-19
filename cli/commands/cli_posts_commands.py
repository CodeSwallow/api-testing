import click
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
