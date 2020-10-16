import click
import os
from lib.helpers.common import get_monitor_input, get_position, list_monitors
from pathlib import Path
import json
import sys

def make_config():
    monitors = list_monitors()
    config = {}

    click.echo('Select the monitor you want to be your primary:')
    primary = get_monitor_input(monitors)
    config['primary'] = monitors.get(primary)
    del monitors[primary]
    value = get_position()
    config[value] = [monitors.get(i) for i in monitors.keys()][0]
    home = str(Path.home())
    filename = f'{home}/.config/screens/config.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        json.dump(config, f, indent=4)

    click.echo(f'Config saved at {filename}')
    sys.exit(0)
