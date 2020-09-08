from setuptools import setup, find_packages

setup(
    name = 'kazoo',
    version = '0.1.0',
    url = '',
    description = '',
    packages = find_packages(),
    install_requires = [
        # Github Private Repository
        'https://github.com/NMTruongGiang/kazoo_py37.git#egg=kazoo'
    ]
)
