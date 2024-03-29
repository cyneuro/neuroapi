import os
from setuptools import setup, find_packages

__version__ = '0.1'

setup(
    name='neuroapi',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-restful',
        'flask-migrate',
        'flask-jwt-extended',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'python-dotenv',
        'passlib',
        'apispec[yaml]',
        'apispec-webframeworks',
        'webargs'
    ],
    entry_points={
        'console_scripts': [
            'neuroapi = neuroapi.manage:cli'
        ]
    }
)
