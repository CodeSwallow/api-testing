import click
from cli.commands import cli_users_commands as usr
from cli.commands import cli_todos_commands as tds
from cli.commands import cli_comments_commands as cms
from cli.commands import cli_posts_commands as pst


@click.group()
def cli():
    """
        CLI app for making calls to endpoints at https://gorest.co.in/
    """
    pass


@cli.group()
def users():
    """
        CLI app for making calls to endpoints at https://gorest.co.in/
        \nEndpoint: '/users'
    """
    pass


users.add_command(usr.get_list)
users.add_command(usr.get_detail)
users.add_command(usr.post)
users.add_command(usr.put)
users.add_command(usr.patch)
users.add_command(usr.delete)
users.add_command(usr.get_posts)
users.add_command(usr.get_todos)
users.add_command(usr.create_post)
users.add_command(usr.create_todo)


@cli.group()
def todos():
    """
        CLI app for making calls to endpoints at https://gorest.co.in/
        \nEndpoint: '/todos'
    """
    pass


todos.add_command(tds.get_list)
todos.add_command(tds.get_detail)


@cli.group()
def posts():
    """
        CLI app for making calls to endpoints at https://gorest.co.in/
        \nEndpoint: '/posts'
    """
    pass


posts.add_command(pst.get_list)
posts.add_command(pst.get_detail)


@cli.group()
def comments():
    """
        CLI app for making calls to endpoints at https://gorest.co.in/
        \nEndpoint: '/comments'
    """
    pass


comments.add_command(cms.get_list)
comments.add_command(cms.get_detail)
