#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Diego Hurtado
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from setuptools import setup, find_packages


def read(filename):
    """
    Read a file relative to setup.py location.
    """
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, filename)) as fd:
        return fd.read()


def find_version(filename):
    """
    Find package version in file.
    """
    import re
    content = read(filename)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def find_requirements(filename):
    """
    Find requirements in file.
    """
    import string
    content = read(filename)
    requirements = []
    for line in content.splitlines():
        line = line.strip()
        if line and line[:1] in string.ascii_letters:
            requirements.append(line)
    return requirements


setup(
    name='opentelemetry_python_autoagent_flask',
    version=find_version('lib/opentelemetry_python_autoagent_flask/__init__.py'),
    package_dir={'': 'lib'},
    packages=find_packages('lib'),

    # Dependencies
    install_requires=find_requirements('requirements.txt'),

    # Metadata
    author='Diego Hurtado',
    author_email='diego.hurtado@toptal.com',
    description=(
        'Flask Plugin for the OpenTelemetry Python AutoAgent'
    ),
    long_description=read('README.rst'),
    url='https://opentelemetry_python_autoagent_flask.readthedocs.org/',
    keywords='opentelemetry_python_autoagent_flask',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
