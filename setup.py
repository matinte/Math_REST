from setuptools import setup, find_packages

setup(
    name='Operations',
    version='0.1.0',
    description='Operations logic associated to REST service',
    packages=find_packages(include=['Math_REST', 'Math_REST.*'])
)
