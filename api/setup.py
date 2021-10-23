import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Copy requirements from requirements.txt
with open(os.path.join(here, 'requirements.txt'), 'r') as f:
    INSTALL_REQUIRES = [line.strip() for line in f.readlines()]

setup(
    name="app",
    version="0.0.1",
    author="Enzo Casasola",
    description="App",
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
)
