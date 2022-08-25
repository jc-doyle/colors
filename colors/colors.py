import chevron
import pickle
from pathlib import Path
from .recipient import Recipient

from .common import print_err, parse_yaml, Config

SCHEME_ENV = 'COLORSCHEME'


class Colors:

    def __init__(self, dir):
        self.pickle_file = dir / '.current'
        self.cfg = self.__get_config(dir)
        self.schemes = self.__fetch_schemes(dir)
        self.templates = self.__fetch_templates(dir)
        self.current = self.__get_current()

    def __get_config(self, dir: Path):
        config_path = dir / 'config.yaml'
        if config_path.is_file():
            return Config(config_path)
        else:
            print_err(f'"config.yaml" not found in "{dir}"\nAborted')

    def __get_current(self):
        if self.pickle_file.is_file():
            with self.pickle_file.open("rb") as f:
                current = pickle.load(f)
        else:
            current = None

        return current

    def __fetch_schemes(self, dir: Path):
        scheme_dir = dir / 'schemes'
        if scheme_dir.is_dir():
            schemes = {}
            for child in scheme_dir.iterdir():
                items = parse_yaml(child)
                schemes[child.stem] = items

            return schemes
        else:
            print_err(f'No scheme directory found in "{dir}"')

    def __fetch_templates(self, dir):
        template_dir = dir / 'templates'
        if template_dir.is_dir():
            templates = {}
            for child in template_dir.iterdir():
                with child.open() as f:
                    templates[child.stem] = f.read()
            return templates
        else:
            print_err(f'No scheme directory found in "{dir}"')

    def get(self, name):
        if name in self.schemes:
            return self.schemes[name]
        else:
            print_err(f'Colorscheme {name} not found')

    def list(self):
        for name in self.schemes:
            if name == self.current:
                print(f'-> {name}')
            else:
                print(f'   {name}')

    def inject(self, name, verbose=False):
        completed = []
        failed = []

        if name in self.schemes:
            scheme = self.schemes[name]

            for program_name, content in self.templates.items():
                if program_name in self.cfg.PATHS:
                    recipient_path = Path(self.cfg.PATHS[program_name])
                    data = chevron.render(content, scheme)

                    r = Recipient(recipient_path, data)
                    r.write()

                    completed.append(program_name)
                else:
                    failed.append(program_name)

            if verbose:
                if len(completed) > 0:
                    print(f'Updated: {", ".join(completed)}')

                if len(failed) > 0:
                    print(f'No configuration file found: {", ".join(failed)}')
        else:
            print_err(f'Colorscheme "{name}" not found.')

        self.__save(name)

    def __save(self, name):
        if name in self.schemes:
            self.current = name
            print(f'-> {self.current}')

            with self.pickle_file.open("wb+") as f:
                pickle.dump(self.current, f)
