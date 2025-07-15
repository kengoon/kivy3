#!/usr/bin/env python

from setuptools import find_packages, setup
from os.path import join, dirname
from os import walk
from pathlib import Path

examples = {}
for root, subFolders, files in walk('examples'):
    for fn in files:
        ext = fn.split('.')[-1].lower()
        filename = join(root, fn)
        directory = '%s%s' % ('share/kivy3-', dirname(filename))
        if directory not in examples:
            examples[directory] = []
        examples[directory].append(filename)


def glob_paths(*patterns, excludes=('.pyc', )):
    files = []
    base = Path(join(dirname(__file__), 'kivy3'))

    for pat in patterns:
        for f in base.glob(pat):
            if f.suffix in excludes:
                continue
            files.append(str(f.relative_to(base)))
    return files

setup(
    name='kivy3',
    version='0.1',
    description='Kivy extensions for 3D graphics',
    author='Niko Skrypnik',
    author_email='nskrypnik@gmail.com',
    package_dir={'kivy3': 'kivy3'},
    package_data={'kivy3': glob_paths('**/*.glsl', '**/*.png')},
    packages=find_packages(exclude=("tests",)),
    data_files=list(examples.items()),
    install_requires=['kivy']
)
