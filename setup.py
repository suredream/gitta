# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""
import re
from setuptools import setup

version = re.search('^__version__\s*=\s*"(.*)"',
                    open('gitta/gitta.py').read(), re.M).group(1)

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="cmdline-gitta",
    packages=["gitta"],
    entry_points={"console_scripts": ['gitta = gitta.gitta:main']},
    version=version,
    description="my pip environments and snippets manager.",
    long_description=long_descr,
    author="Jun Xiong",
    author_email="junxiong360@gmail.com",
    url="https://github.com/suredream/gitta",
)
