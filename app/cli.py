import click
from flask.cli import with_appcontext

from .models import db


@click.command('create_table')
@with_appcontext
def create_table():
    """Create db tables"""
    db.create_all()


@click.command('hello')
@click.option('--name', default='World')
def hello(name):
    """Say hello"""
    click.echo(f'Hello, {name}!')
