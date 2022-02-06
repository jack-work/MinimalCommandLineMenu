from setuptools import setup, find_packages
import codecs
import os

VERSION = ':-D'
DESCRIPTION = 'A minimal Python command line menu'

setup(
    name='MinimalCommandLineMenu',
    version=VERSION,
    author='John Kelliher',
    author_email='jackwkelliher@gmail.com',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=open('README.md', 'r').read(),
    packages=find_packages(),
    install_requires=[],
    keywords=['menu','command line'],
    classifiers=['A very simple tool to practice Python packages']
)