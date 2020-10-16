from lib.helpers.common import get_monitor_input, get_position, list_monitors
from pathlib import Path
import json
import click
import subprocess

def apply_config():
    if len(list_monitors().keys()) < 2:
        click.echo('No other monitors found')
        sys.exit(-1)

    home = str(Path.home())
    filename = f'{home}/.config/screens/config.json'
    config_file = Path(filename)
    if not config_file.is_file():
        click.echo('No config file found! Make one right now!!')
        make_config()
    with open(filename) as f:
        data = json.load(f)

    primary = data['primary']
    del data['primary']
    other = list(data.keys())[0]

    pre = f'--{other}-of' if other == 'right' or other == 'left' else f'--{other}'
    suffix = f'--auto --primary {pre} ' + primary
    prefix = f'xrandr --output {data.get(other)} '
    command = prefix + suffix
    click.echo(command)
    proc = subprocess.getoutput(command)

