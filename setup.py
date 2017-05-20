try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Binary search',
    'author': 'Mariana Souza',
    'url': 'N/A.',
    'download_url': 'N/A',
    'author_email': 'xxxxxxx@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': ['binary_search.py', 'generating_primenum.py'],
    'name': 'binary-search'
}

setup(**config)