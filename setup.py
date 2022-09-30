from setuptools import setup

setup(
    name='alerts',
    version=1.0,
    packages=['alerts'],
    install_requires=['click', 'requests', 'pytest', 'pyyaml'],
    entry_points={'console_scripts': ['alert = alerts.cli:cli']}
)
