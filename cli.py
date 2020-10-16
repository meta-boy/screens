import click

from lib import commands

@click.group()
def cli():
    pass

cli.add_command(commands.config)

if __name__ == '__main__':
    cli()
    