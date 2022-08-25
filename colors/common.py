import sys
import yaml
from pathlib import Path
from yaml.error import YAMLError

XDG = 'XDG_CONFIG_HOME'
COLOR_ENV = 'COLOR_DIR'


def print_err(string):
    print(string)
    sys.exit(1)


def parse_yaml(path: Path):
    try:
        with path.open() as f:
            items = yaml.safe_load(f)
            return items
    except YAMLError:
        print_err(f'Invalid YAML file at "{path}"')


class Config:

    def __init__(self, path):
        raw_yaml = parse_yaml(path)
        self.__parse(raw_yaml)

    def __parse(self, data):
        if 'general' in data:
            self.GENERAL = data.pop('general')
        else:
            self.GENERAL = None

        self.PATHS = data
