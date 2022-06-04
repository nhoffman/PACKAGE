import os
import subprocess
import setuptools

subprocess.call(
    ('mkdir -p PACKAGE/data && '
     'git describe --tags --dirty > PACKAGE/data/ver.tmp '
     '&& mv PACKAGE/data/ver.tmp PACKAGE/data/ver '
     '|| rm -f PACKAGE/data/ver.tmp'),
    shell=True, stderr=open(os.devnull, "w"))

from PACKAGE import __version__

package_data = ['data/*']

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PACKAGE",
    version=__version__,
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)

# params = {'author': 'Your name',
#           'author_email': 'Your email',
#           'description': 'Package description',
#           'name': 'PACKAGE',
#           'packages': setuptools.find_packages(),
#           'package_dir': {'PACKAGE': 'PACKAGE'},
#           'entry_points': {
#               'console_scripts': ['PACKAGE = PACKAGE.scripts.main:main']
#           },
#           'version': __version__,
#           'package_data': {'PACKAGE': package_data},
#           'test_suite': 'tests',
#           'cmdclass': {'check_version': CheckVersion},
#           'install_requires': [
#           ]}

# setuptools.setup(**params)
