flake8-sfs - Python String Formatting Style Plugin
==================================================

.. image:: https://img.shields.io/pypi/v/flake8-sfs.svg
   :alt: Released on the Python Package Index (PyPI)
   :target: https://pypi.org/project/flake8-sfs/
.. image:: https://img.shields.io/conda/vn/conda-forge/flake8-sfs.svg
   :alt: Released on Conda
   :target: https://anaconda.org/conda-forge/flake8-sfs
.. image:: https://img.shields.io/travis/peterjc/flake8-sfs/master.svg
   :alt: Testing with TravisCI
   :target: https://travis-ci.org/peterjc/flake8-sfs/branches
.. image:: https://img.shields.io/pypi/dm/flake8-sfs.svg
   :alt: PyPI downloads
   :target: https://pypistats.org/packages/flake8-sfs
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :alt: Code style: black
   :target: https://github.com/python/black

Introduction
------------

This is an MIT licensed flake8 plugin for enforcing a Python string formatting
preference. It is available to install from the `Python Package Index (PyPI)
<https://pypi.org/project/flake8-sfs/>`_.

For historical reasons, the Python programming language has accumlated multiple
ways to do string formatting. The three main ones are:

* Percent operator, as in this example:

    >>> name = "Peter"
    >>> price = 1.2
    >>> print("Hello %s, do you have $%0.2f?" % (name, price))
    Hello Peter, do you have $1.20?

* Format method, available since Python 2.6,

    >>> name = "Peter"
    >>> price = 1.2
    >>> print("Hello {}, do you have ${:0.2f}?".format(name, price))
    Hello Peter, do you have $1.20?

* f-strings, available since Python 3.6,

    >>> name = "Peter"
    >>> price = 1.2
    >>> print(f"Hello {name}, do you have ${price:0.2f}?")

We are spoilt for choice, but quoting the `Zen of Python
<https://www.python.org/dev/peps/pep-0020/>`_, *There should be one - and
preferably only one - obvious way to do it*. This flake8 plugin exists to let
you define which of these styles your project allows.

For example, if you accept that f-strings are best, you could run a tool like
`flynt <https://github.com/ikamensh/flynt>`_ to automatically convert all your
code - and then use this flake8 plugin to enforce the style.

Alternatively, you might have a large legacy codebase with lots of the percent
formatting - yet want to gradually move to f-strings. Here you could use this
plugin to enforce a rule allowing those but rejecting the string format method.

Or you might the the old ways are the best, and configure flake8 to ignore the
percent formatting but treat either the format method or f-strings as errors.

By default this plugin complains about all three styles - we expect you to make
an explicit choice and configure which codes to ignore.

Flake8 Validation codes
-----------------------

Early versions of flake8 assumed a single character prefix for the validation
codes, which became problematic with collisions in the plugin ecosystem. Since
v3.0, flake8 has supported longer prefixes therefore this plugin uses ``SFS``
as its prefix (short for String Format Style).

====== =======================================================================
Code   Description
------ -----------------------------------------------------------------------
SFS100 Bytes literal formatting using percent operator.
SFS101 String literal formatting using percent operator.
SFS102 String literal formatting using .format method.
SFS103 String literal formatting using f-string.
SFS104 String formatting with str.format('...', ...) directly.
====== =======================================================================


Installation and usage
----------------------

Python 3.6 or later is required (as we use need to parse the Python syntax
which may include f-strings).

We recommend installing the plugin using pip, which handles the dependencies::

    $ pip install flake8-sfs

Alternatively, if you are using the Anaconda packaging system, the following
command will install the plugin with its dependencies::

    $ conda install -c conda-forge flake8-sfs

The new validator should be automatically included when using ``flake8`` which
may now report additional validation codes starting with ``SFS`` (as defined
above). For example::

    $ flake8 example.py

You can request only the ``SFS`` codes be shown using::

    $ flake8 --select SFS example.py

Similarly you might add particular SFS validation codes to your flake8
configuration file's select or ignore list.


Configuration
-------------

We assume you are familiar with `flake8 configuration
<http://flake8.pycqa.org/en/latest/user/configuration.html>`_.

Unless your code performs no string formatting at all (which would be unusual),
you should tell flake8 to ignore at least one of this plugin's violation codes.
For example::

    [flake8]
    extend-ignore =
        # Ignore f-strings, we like them:
        SFS103,

Note that flake8 allows splitting comma separated lists over multiple lines,
and allows including of hash comment lines.


Version History
---------------

======= ========== ===========================================================
Version Released   Changes
------- ---------- -----------------------------------------------------------
v0.0.2  2020-01-12 - Added ``SFS104`` for using ``str.format("...", ...)``.
v0.0.1  2020-01-11 - Initial public release.
======= ========== ===========================================================


Developers
----------

This plugin is on GitHub at https://github.com/peterjc/flake8-sfs

To make a new release once tested locally and on TravisCI::

    $ git tag vX.Y.Z
    $ python setup.py sdist --formats=gztar
    $ twine upload dist/flake8-sfs-X.Y.Z.tar.gz
    $ git push origin master --tags

The PyPI upload should trigger an automated pull request updating the
`flake8-sfs conda-forge recipe
<https://github.com/conda-forge/flake8-sfs-feedstock/blob/master/recipe/meta.yaml>`_.


TODO
----

- Can/should we spot byte formatting?
- Can we spot pointless f-strings? See flake8-pie's PIE782 code.