from setuptools import find_packages
from setuptools import setup

setup(
    name='cmrosutils',
    version='0.1.0',
    packages=find_packages(
        include=('cmrosutils', 'cmrosutils.*')),
)
