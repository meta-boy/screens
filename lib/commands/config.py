import click
from lib.helpers.make import make_config
from lib.helpers.apply import apply_config
from lib.helpers.show import show_config

@click.command()
@click.option('--show', is_flag=True)
@click.option('--make', is_flag=True)
@click.option('--apply', is_flag=True)
def config(show, make, apply):
    if make:
        make_config()
    if apply:
        apply_config()

    if show:
        show_config()






