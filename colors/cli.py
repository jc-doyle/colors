import argparse
from .common import print_err
from .colors import Colors

NAME = "colors"
DESC = "A utility to change, view & manipulate colorschemes."
parser = argparse.ArgumentParser(prog=NAME, description=DESC)
parser.add_argument('--set', '-s', action='store_true')
parser.add_argument('--list', '-l', action='store_true')
parser.add_argument("name", nargs='?', help="update current colorscheme")


def catch_keyboard_interrupt(func):
    """Decorator for catching KeyboardInterrupt and quitting gracefully."""

    def decorated(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            print_err("Interrupt signal received.")

    return decorated


@catch_keyboard_interrupt
def run():
    args = parser.parse_args()

    c = Colors()
    if args.set:
        if args.name:
            c.inject(args.name)
        elif c.current is not None:
            c.inject(c.current)
    elif args.list:
        print('list')
    else:
        print('show colors')


run()
