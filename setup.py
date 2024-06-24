import subprocess
from setuptools import setup, find_packages



def read_requirements():
    with open('requirements.txt') as req_file:
        return req_file.readlines()

setup(
    name='rainbow_plot',
    version='0.1',
    packages=find_packages(),
    description='Semi-Circle Pie Chart for Python',
    author='Gabriel Rashidi',
    url='https://github.com/grashidi/rainbow_plot',
    install_requires=read_requirements(),
)


