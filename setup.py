from os import path
from codecs import open
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rook_number',
    version='0.0.1',

    description='A rook number simulator.',
    long_description=long_description,

    url='https://github.com/liamlundy/RookNumber',

    license='GPLv3',

    author='Liam Lundy',
    author_email='llundy@gmail.com',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,

    install_requires=[],
    setup_requires=[
      'pytest-runner',
    ],
    tests_require=[
      'pytest',
      'coverage'
    ],

)
