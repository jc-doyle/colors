import os
import argparse
from pathlib import Path
from .common import print_err, COLOR_ENV, XDG
from .colors import Colors
from .picker import Picker

NAME = "colors"
DESC = "A utility to change & view colorschemes."
parser = argparse.ArgumentParser(prog=NAME, description=DESC)
parser.add_argument('--set', '-s', action='store_true')
parser.add_argument('--list', '-l', action='store_true')
parser.add_argument('--print', '-p', action='store_true')
parser.add_argument('--verbose', '-v', action='store_true')
parser.add_argument('--current', '-c', action='store_true')
parser.add_argument("name", nargs='?', help="colorscheme name [optional]")

if COLOR_ENV in os.environ:
    BASE_DIR = Path(os.environ[f'{COLOR_ENV}'])
elif XDG in os.environ:
    BASE_DIR = Path(os.environ[f'{XDG}']) / 'colors'
else:
    BASE_DIR = Path().home() / '.colors'
    print(
        f'Neither COLOR_DIR nor XDG_CONFIG_HOME variables set\n Reverting to {BASE_DIR}'
    )


def catch_keyboard_interrupt(func):
    """Decorator for catching KeyboardInterrupt and quitting gracefully."""

    def decorated(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            print_err("Interrupt signal received.")

    return decorated


def injector(colors: Colors, args):
    if args.name:
        colors.inject(args.name, args.verbose)
    elif colors.current is not None:
        colors.inject(colors.current, args.verbose)
    else:
        print_err('No current scheme found')


def picker(c: Colors, args):
    if args.name:
        color = c.get(args.name)
        p = Picker(color)
        p.run()
    elif c.current is not None:
        current = c.get(c.current)
        p = Picker(current)
        p.run()
    else:
        print_err('No current scheme found')


def default(c: Colors, args):
    if args.name:
        injector(c, args)
    else:
        injector(c, args)
        picker(c, args)


def current(c: Colors, args):
    if c.current is not None:
        print(c.current)


@catch_keyboard_interrupt
def run():
    args = parser.parse_args()
    c = Colors(BASE_DIR)

    if args.list:
        c.list()
    elif args.current:
        current(c, args)
    elif args.set:
        injector(c, args)
    elif args.print:
        picker(c, args)
    else:
        default(c, args)
