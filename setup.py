import os
import subprocess
import setuptools

subprocess.call(
    ('mkdir -p src/PACKAGE/data && '
     'touch src/PACKAGE/data/ver && '
     'git describe --tags --dirty > src/PACKAGE/data/ver.tmp '
     '&& mv src/PACKAGE/data/ver.tmp src/PACKAGE/data/ver '
     '|| rm -f src/PACKAGE/data/ver.tmp'),
    shell=True, stderr=open(os.devnull, "w"))

with open('src/PACKAGE/data/ver') as f:
    version = f.read().strip() or '0.0.0'

package_data = ['data/*']

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PACKAGE",
    version=version,
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.example.com",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src', 'PACKAGE': 'src/PACKAGE'},
    package_data={'PACKAGE': package_data},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        'console_scripts': ['PACKAGE = PACKAGE.main:main']
    },
    python_requires=">=3.8",
    install_requires=[],
)
