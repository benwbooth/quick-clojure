'''
    quick
    -------------------

    Run clojure scripts and lein commands quickly using a persistent nREPL session.

    Links
    `````
    * `development version <https://github.com/benwbooth/quick-clojure>`_
'''

import os
from setuptools import setup, find_packages

setup(name="quick-clojure",
      version='0.10',
      packages=find_packages(),
      # metadata for upload to PyPI
      author="Ben Booth",
      author_email="benwbooth@gmail.com",
      description="Run clojure scripts and lein commands quickly using a persistent nREPL session.",
      long_description=__doc__,
      test_suite='test',
      license="EPL v1.0",
      keywords="clojure repl nrepl leiningen lein",
      url="https://github.com/benwbooth/quick-clojure",
      zip_safe=True,
      platforms='any',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Interpreters',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      scripts=['quick','quick-exec','quick-exec-p'],
      install_requires=['nrepl-python-client','future'])
