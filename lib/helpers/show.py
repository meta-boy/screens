from pathlib import Path
import json
import click
from lib.helpers.make import make_config 

def show_config():
    home = str(Path.home())
    filename = f'{home}/.config/screens/config.json'
    config_file = Path(filename)
    if not config_file.is_file():
        click.echo('No config file found! Make one right now!!')
        make_config()
    with open(filename) as f:
        data = json.load(f)
    click.echo(json.dumps(data, indent=4))