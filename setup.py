#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import re

# Set dependencies, we need sphinx to build doc and numpy for arrays
dependencies = ['sphinx','numpy','future','pyfits']

# Auto-generate documentation
import sphinx

# Add doc directory to install-prefix directory
datafiles=[]
for d, folders, files in os.walk('doc/build/html'):
  dir_inst='doc/'+re.sub('doc/build/','',d)
  datafiles.append((dir_inst, [os.path.join(d,f) for f in files]))


# Automatically build html documentation
# For example:
#   format = 'html'
#   sphinx-src-dir = './doc'
#   sphinx-build-dir = './doc/build'
sphinx.build_main(['setup.py', '-b', 'html', './doc/source', './doc/build/html'])

# Do the actual setup
setup(name='pyspex',
      version='0.2',
      description='SPEX Python tools',
      author='SPEX development team',
      author_email='j.de.plaa@sron.nl',
      url='https://www.sron.nl/spex',
      packages=find_packages(),
      include_package_data = True,
      package_data={'':['*.rst']},
      data_files=datafiles,
      install_requires=dependencies,
      )