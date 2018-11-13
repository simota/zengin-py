# -*- coding: utf-8 -*-

import sys
import os
import re

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

here = os.path.dirname(__file__)
package_path = os.path.join(here, 'zengin_code')

version = ''
with open(os.path.join(package_path, '__init__.py'), 'r') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'\n", re.S).match(f.read()).group(1)

version = '{0}.{1}'.format(version, open(os.path.join(
    package_path, 'source-data', 'data', 'updated_at'
), 'r').read().strip())

readme = open(os.path.join(here, 'README.rst')).read()

requires = [
    'six',
]

tests_require = [
    'pytest-cov',
    'pytest',
]

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries',
]


setup(
    name='zengin_code',
    version=version,
    description='bank codes and branch codes for Japanese.',
    long_description=readme,
    url='https://github.com/zengin-code/zengin-py',
    author='Zengin Code',
    author_email='zengin-code@zeny.io',
    classifiers=classifiers,
    keywords=['zengin', 'bank', 'japanese'],
    install_requires=requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={
        'zengin_code': [
            'source-data/data/md5', 'source-data/data/updated_at',
            'source-data/data/*.json', 'source-data/data/branches/*.json'
        ]
    },
    license='MIT',
)
