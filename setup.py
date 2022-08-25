from setuptools import setup

setup(
    name="colors",
    version="0.2.8",
    description="a colorscheme builder",
    packages=["colors"],
    author="Jonathan Doyle",
    install_requires=["chevron", "pyyaml", "rich"],
    python_requires=">=3.5",
    entry_points={"console_scripts": ["colors = colors.main:run"]},
)
