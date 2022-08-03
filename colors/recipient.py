import re
import sys

TOKEN = re.compile(r"^.*-- colors --.*$")

class Recipient:

    def __init__(self, path, replacement):
        self.path = path
        self.replacement = replacement.split('\n')
        self.content = self._get_content(self.path)
        self.matched_lines = self._match_lines()

    def _get_content(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError as e:
            print(f'File "{self.path}" not found.')
            sys.exit(1)

        return content.split('\n')

    def _match_lines(self):
        matched_lines = []
        for i, line in enumerate(self.content):
            if TOKEN.match(line):
                matched_lines.append(i)

        if len(matched_lines) != 2:
            print(f'No correct matching pattern found in "{self.path}". Aborted.')
            sys.exit(1)

        return matched_lines
        
    def _replaced_lines(self):
        content_before = self.content[:self.matched_lines[0] + 1]
        content_after = self.content[self.matched_lines[1]:]

        return content_before + self.replacement + content_after

    def write(self):
        content = "\n".join(self._replaced_lines())

        with open(self.path, "w", encoding="utf-8") as f:
            f.write(content)
