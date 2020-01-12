"""Setup file for building/installing flake8-sfs."""

from __future__ import with_statement

from setuptools import setup


def get_version(fname="flake8_sfs.py"):
    """Parse our source code to get the current version number."""
    with open(fname) as f:
        for line in f:
            if line.startswith("__version__"):
                return eval(line.split("=")[-1])


setup(
    name="flake8-sfs",
    version=get_version(),
    description="Python String Formatting Style (SFS) plugin for flake8",
    long_description=open("README.rst").read(),
    license="MIT",
    author="Peter J. A. Cock",
    author_email="p.j.a.cock@googlemail.com",
    url="https://github.com/peterjc/flake8-sfs",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Framework :: Flake8",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    keywords="strings, formatting, style, f-string",
    py_modules=["flake8_sfs"],
    install_requires=["flake8 >= 3.0.0"],
    entry_points={"flake8.extension": ["SFS = flake8_sfs:StringFormatStyleChecker"]},
)
