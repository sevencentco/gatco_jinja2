# -*- coding: utf-8 -*-
import re
from os import path
from setuptools import find_packages, setup

ROOT_DIR = path.abspath(path.dirname(__file__))

DESCRIPTION = 'Gatco-Jinja2 - Jinja2 template engine support for Gatco / Sanic'
LONG_DESCRIPTION = open(path.join(ROOT_DIR, 'README.rst')).read()
VERSION = re.search(
    "__version__ = '([^']+)'",
    open(path.join(ROOT_DIR, 'gatco_jinja2', '__init__.py')).read()
).group(1)


setup(
    name='Gatco-Jinja2',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url='https://github.com/gonrin/gatco_jinja2/',
    author='cuongnc.coder and contributors',
    author_email='cuongnc.coder@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        'gatco','jinja2<=2.11.3'
    ],
    extras_require={
        'dev': [
            'aiohttp',
            'flake8',
            'pytest',
            'pytest-cov',
            'Sphinx',
            'tox',
            'twine',
        ],
    },
    zip_safe=False,
    platforms='any',
)
