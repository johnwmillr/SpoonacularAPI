# Spoonacular API
# Copyright 2018 John W. Miller
# See LICENSE for details.

import re
import os
from setuptools import find_packages, setup

VERSIONFILE = "spoonacular/__init__.py"
ver_file = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, ver_file, re.M)

if mo:
    version = mo.group(1)
else:
    raise RuntimeError(
        "Unable to find version string in {}".format(VERSIONFILE))

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

setup(name="spoonacular",
      version=version,
      description="A Python wrapper for the Spoonacular API",
      long_description=README,
      long_description_content_type="text/markdown",
      license="MIT",
      author="John W. Miller",
      url="https://github.com/johnwmillr/SpoonacularAPI",
      packages=find_packages(exclude=['tests']),
      install_requires=["requests"],
      keywords="spoonacular API food recipes ingredients cuisine groceries",
      python_requires=">=3.*",
      classifiers=[
              'Topic :: Software Development :: Libraries',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
      ])
