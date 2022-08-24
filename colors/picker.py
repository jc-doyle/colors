import os
from collections import defaultdict
from subprocess import Popen, PIPE

from rich.console import Console
from rich.style import Style

from .common import print_err

ROW_HEIGHT = 8


class Picker:

    def __init__(self, colors):
        self.colors = list(colors.items())

    def print(self):
        os.system('clear')
        c = Console(color_system="truecolor", highlight=False)
        rows = defaultdict(list)

        for i, color in enumerate(self.colors):
            rows[i % ROW_HEIGHT].append((i, color[1]))

        for row, colors in rows.items():
            for color in colors:
                c.print(f'{color[0]:2d}', end=' ', style=color[1])
                print('∈', end=' ')
                s = Style(bgcolor=color[1], color=self.colors[0][1])
                c.print(f'{color[1][1:]}', end='', style=s)
                print('  ', end=' ')
            print()

    def run(self):
        self.print()
        num_input = input(' > ')

        while input != 'q':
            try:
                self.print()
                color = self.colors[int(num_input)][1]
                p = Popen(['xclip'], stdin=PIPE)
                p.communicate(input=color.encode())
                num_input = input('·> ')
            except ValueError:
                exit(0)
