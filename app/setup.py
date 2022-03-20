import os
from setuptools import setup

os.environ['PBR_VERSION'] = "1.0.0"

# setup.py
setup(setup_requires=["pbr"],
      pbr=True)
