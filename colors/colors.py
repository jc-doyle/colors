import yaml
import chevron
import os
import sys
import pickle
from .recipient import Recipient
from .common import print_err

try:
    BASE_DIR = os.environ['COLOR_DIR']
except KeyError:
    print_err('Environment variable "COLOR_DIR" not found. Aborted.')

CONFIG_PATH = f'{BASE_DIR}config.yaml'
SCHEME_DIR = f'{BASE_DIR}schemes/'
TEMPLATE_DIR = f'{BASE_DIR}templates/'
PICKLE_FILE = f'{BASE_DIR}current.pkl'


class Colors:

    def __init__(self):
        self.schemes = self._fetch_schemes(SCHEME_DIR)
        self.templates = self._fetch_templates(TEMPLATE_DIR)
        self.current = self._get_current()

    def _get_current(self):
        try:
            with open(PICKLE_FILE, "rb") as f:
                current = pickle.load(f)
        except (FileNotFoundError, TypeError):
            current = None

        return current

    def _fetch_schemes(self, dir):
        with os.scandir(dir) as iterator:
            schemes = {}
            for item in iterator:
                if item.name.endswith(".yaml") and item.is_file():
                    name = item.name.split('.')[0]
                    schemes[name] = self.__fetch_scheme(item.path)
            return schemes

    def _fetch_templates(self, dir):
        with os.scandir(dir) as iterator:
            templates = {}
            for item in iterator:
                if item.name.endswith(".mustache") and item.is_file():
                    name = item.name.split('.')[0]
                    templates[name] = item.path
            return templates

    def __fetch_scheme(self, path):
        with open(path, 'r') as f:
            items = yaml.safe_load(f)
            return items

    def inject(self, name):
        with open(CONFIG_PATH, 'r') as f:
            config = yaml.safe_load(f)

        for program_name, path in self.templates.items():
            try:
                with open(path, 'r') as f:
                    if program_name in config:
                        try:
                            rendered_scheme = chevron.render(
                                f, self.schemes[name])
                            recipient = Recipient(config[program_name],
                                                  rendered_scheme)
                        except KeyError:
                            print_err(f'Colorscheme "{name}" not found.')
                        recipient.write()
                        print(f'Updated {program_name}.')
                    else:
                        print(f'No configuration found for "{program_name}".')
            except FileNotFoundError:
                print_err(f'File "{path}" not found.')

        if name in self.schemes:
            self.current = name

            with open(PICKLE_FILE, "wb+") as f:
                pickle.dump(self.current, f)
