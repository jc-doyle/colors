import re
import sys
import os
from pathlib import Path
from .common import print_err, XDG

TOKEN = re.compile(r"^.*-- colors --.*$")


class Recipient:

    def __init__(self, path: Path, replacement):
        self.path = self.__handle_path(path)
        self.replacement = replacement.split('\n')
        self.content = self.__get_content(self.path)
        self.matched_lines = self.__match_lines()

    def __handle_path(self, path: Path):
        if path.is_file():
            return path
        elif path.expanduser().is_file():
            return path.expanduser()
        elif XDG in os.environ:
            return os.environ[XDG] / path.expanduser()
        else:
            print_err(f'File "{path}" not found.')

    def __get_content(self, path):
        with self.path.open('r') as f:
            content = f.read()

        return content.split('\n')

    def __match_lines(self):
        matched_lines = []
        for i, line in enumerate(self.content):
            if TOKEN.match(line):
                matched_lines.append(i)

        if len(matched_lines) != 2:
            print(
                f'No correct matching pattern found in "{self.path}"\nAborted'
            )
            sys.exit(1)

        return matched_lines

    def __replaced_lines(self):
        content_before = self.content[:self.matched_lines[0] + 1]
        content_after = self.content[self.matched_lines[1]:]

        return content_before + self.replacement + content_after

    def write(self):
        content = "\n".join(self.__replaced_lines())

        with self.path.open("w", encoding="utf-8") as f:
            f.write(content)
