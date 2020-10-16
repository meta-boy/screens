import re
import subprocess
from typing import Dict
import sys
import json
import os
import click

def list_monitors() -> Dict:
    proc = subprocess.getoutput('xrandr --listmonitors')
    monitors = {}
    # counter = 0
    res = re.findall(r'  (.*)', proc)
    for i in range(len(res)):
        monitors[i] = res[i]
    return monitors


def get_monitor_input(monitors: dict) -> int:
    value = click.prompt(
        '\n'.join(f'{k}. {v}' for k, v in monitors.items()) + '\n', type=int)

    if value in range(len(monitors.keys())):
        return value
    else:
        click.echo('Invalid choice... aborting')
        sys.exit(-1)


def get_position() -> str:
    options = ['right', 'left', 'above', 'below']
    click.echo('Where do you want the other screen to be?\noptions: ')
    value = click.prompt(
        '\n'.join([f'{i}.{options[i]}' for i in range(len(options))]) + '\n', type=int)

    if value in range(len(options)):
        return options[value]
    else:

        click.echo('Invalid choice... aborting')
        sys.exit(-1)
