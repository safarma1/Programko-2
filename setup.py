from setuptools import setup, find_packages

with open('https://raw.githubusercontent.com/safarma1/Programko2/semestral/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='skymap',
    version='1.0.0',
    packages=find_packages(),
    install_requires=requirements, 
    entry_points={
        'console_scripts': [
            'starmap = main.py:main',
        ],
    },
)
