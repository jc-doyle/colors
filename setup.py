from setuptools import setup

from pathlib import Path
dir = Path(__file__).parent
desc = (dir / 'README.md').read_text()

setup(
    name="colors",
    version="0.1",
    description="A [Unix] Colorscheme Generator",
    packages=["colors"],
    author="Jonathan Doyle",
    install_requires=["chevron", "pyyaml", "rich"],
    python_requires=">=3.5",
    entry_points={"console_scripts": ["colors = colors.main:run"]},
    long_description=desc
)
