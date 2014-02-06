'''
    quick
    -------------------

    A quick command launcher for leiningen.

    Links
    `````
    * `development version <https://github.com/benwbooth/quick-clojure>`_
'''

import os

from setuptools import setup, find_packages

# HACK: Pull the version number without requiring the package to be installed
# beforehand, i.e. without using import.
module_path = os.path.join(os.path.dirname(__file__), 'quick')
version_line = [line for line in open(module_path)
                if line.startswith('__version_info__')][0]
__version__ = '.'.join(eval(version_line.split('__version_info__ = ')[-1]))

description = "Quickly launch leiningen commands using a python nREPL client."
classifiers = ['Development Status :: 4 - Beta',
               'Environment :: Console',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Topic :: Software Development :: Interpreters',
               'Topic :: Software Development :: Libraries :: Python Modules',
               'Topic :: Utilities']

setup(name="quick-clojure",
      version=__version__,
      packages=find_packages(),
      # metadata for upload to PyPI
      author="Ben Booth",
      author_email="benwbooth@gmail.com",
      description=description,
      long_description=__doc__,
      test_suite='test',
      license="MIT License",
      keywords="clojure repl nrepl leiningen lein",
      url="https://github.com/benwbooth/quick-clojure",
      zip_safe=True,
      platforms='any',
      classifiers=classifiers,
      scripts=['quick','quick-exec','quick-exec-p'],
      install_requires=['nrepl'])
