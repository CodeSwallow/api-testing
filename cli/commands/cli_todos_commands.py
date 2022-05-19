import click
from services.todo_service import TodoService


@click.command()
@click.option('--page', default=1, help='page number of user list')
@click.option('--user_id', default=None, help='filter by user id')
@click.option('--title', default=None, help='filter by title')
@click.option('--due_on', default=None, help='filter by due on date')
@click.option('--status', default=None, help='filter by status')
def get_list(page, user_id, title, due_on, status):
    """
        Call todos api to retrieve list of todos with optional query params
    """
    filters = {'page': page}
    if user_id is not None:
        filters['user_id'] = user_id
    if title is not None:
        filters['title'] = title
    if due_on is not None:
        filters['due_on'] = due_on
    if status is not None:
        filters['status'] = status
    click.echo("Getting todos...")
    api = TodoService()
    resp = api.get_list(query_params=filters)
    if resp.status_code == 200:
        if len(resp.json()) == 0:
            click.echo('Empty')
        for todo in resp.json():
            click.echo(todo)
    else:
        click.echo(f"Error: {resp.status_code}")


@click.command()
@click.argument('primary_key')
def get_detail(primary_key):
    """
        Call todos api to retrieve todo detail with id (PRIMARY_KEY) given
    """
    click.echo("Todo details...")
    try:
        pk = int(primary_key)
        api = TodoService()
        resp = api.get_detail(pk=pk)
        if resp.status_code == 200:
            click.echo(resp.json())
        elif resp.status_code == 404:
            click.echo(f"Could not find todo with id: {primary_key}")
        else:
            click.echo(f"Error: {resp.status_code}")
    except ValueError:
        click.echo(f"Primary Key must be an integer")
