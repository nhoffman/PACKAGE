import os
import subprocess

from distutils.core import Command
from setuptools import setup, find_packages

subprocess.call(
    ('mkdir -p PACKAGE/data && '
     'git describe --tags --dirty > PACKAGE/data/ver.tmp '
     '&& mv PACKAGE/data/ver.tmp PACKAGE/data/ver '
     '|| rm -f PACKAGE/data/ver.tmp'),
    shell=True, stderr=open(os.devnull, "w"))

from PACKAGE import __version__


class CheckVersion(Command):
    description = 'Confirm that the stored package version is correct'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        with open('PACKAGE/data/ver') as f:
            stored_version = f.read().strip()

        git_version = subprocess.check_output(
            ['git', 'describe', '--tags', '--dirty']).strip()

        assert stored_version == git_version
        print('the current version is', stored_version)


package_data = ['data/*']

params = {'author': 'Your name',
          'author_email': 'Your email',
          'description': 'Package description',
          'name': 'PACKAGE',
          'packages': find_packages(),
          'package_dir': {'PACKAGE': 'PACKAGE'},
          'entry_points': {
              'console_scripts': ['PACKAGE = PACKAGE.scripts.main:main']
          },
          'version': __version__,
          'package_data': {'PACKAGE': package_data},
          'test_suite': 'tests',
          'cmdclass': {'check_version': CheckVersion},
          'install_requires': [
          ]}

setup(**params)
