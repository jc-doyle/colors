#!/usr/bin/python

import os
import sys
import yaml
from subprocess import Popen, PIPE
from rich.console import Console
from rich.style import Style

THEME_DIR = '/home/jonty/other/dotfiles/colors/schemes/'


def int_to_hex(base):
    hex_base = "{:02x}".format(int(base))
    return 'base' + hex_base.upper()


def get_colors(path):
    with open(path, 'r') as f:
        colors = yaml.safe_load(f)
        colors.pop('scheme')
        colors.pop('author')
        return colors


def print_colors():
    os.system('clear')

    console = Console(color_system="truecolor", highlight=False)

    for i in range(0, 8):
        index_left = "{:2d}".format(i)
        color_left = colors[int_to_hex(i)]
        console.print(index_left, end='', style='#' + colors[int_to_hex(3)])
        console.print(' ∈ ', end='', style='#' + colors[int_to_hex(1)])
        console.print(color_left, style='#' + colors[int_to_hex(i)], end=' ')
        console.print('  ',
                      style=Style(bgcolor='#' + colors[int_to_hex(i)]),
                      end=' ')
        console.print('', end=7 * ' ')

        index_right = "{:2d}".format(i + 8)
        color_right = colors[int_to_hex(i + 8)]
        console.print(index_right, end='', style='#' + colors[int_to_hex(3)])
        console.print(' ∈ ', end='', style='#' + colors[int_to_hex(1)])
        console.print(color_right,
                      style='#' + colors[int_to_hex(i + 8)],
                      end=' ')
        console.print('   ',
                      style=Style(bgcolor='#' + colors[int_to_hex(i + 8)]))


def run():
    if len(sys.argv) > 1:
        name = sys.argv[1]
        colors = get_colors(f'{THEME_DIR}{name}/{name}.yaml')
    else:
        colors = get_colors(THEME_DIR + 'dark/dark.yaml')

    print_colors()
    num_input = input(' > ')

    while input != 'q':
        print_colors()
        try:
            hex_code = '#' + colors[int_to_hex(num_input)]
            p = Popen(['xclip'], stdin=PIPE)
            p.communicate(input=hex_code.encode())
            num_input = input('·> ')
        except ValueError as ex:
            exit(0)
