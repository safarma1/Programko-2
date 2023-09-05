from setuptools import setup

setup(
    name='semestral',
    version='1.0.0',
    scripts='main.py',
    install_requires=[
    'geopy',
    'tzwhere',
    'pytz',
    'numpy',
    'matplotlib',
    'skyfield',
    'timezonefinder',
    'pandas',
],
)
