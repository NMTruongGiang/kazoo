from setuptools import setup, find_packages

setup(
    name = 'kazoo',
    version = '0.1.0',
    url = '',
    description = '',
    packages = find_packages(),
    install_requires = [
        # Github Private Repository
        'kazoo @ git+ssh://git@github.com/example_organization/ExampleRepo.git#egg=kazoo'
    ]
)
