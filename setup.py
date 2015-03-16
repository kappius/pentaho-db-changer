#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup

VERSION = __import__('set_db_pdi').__version__

setup(
    name='pentaho-db-changer',
    packages=['set_db_pdi'],
    version=VERSION,
    description='Change dynamically Pentaho database connections from '
                'kjb, ktr and xml files',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst'),
                          'r').read(),
    author='Diogo Munaro Vieira, '
           'Thiago Pereira Fernandes',
    author_email='diogo.mvieira@gmail.com, '
                 'thiago.fernandes210@gmail.com',
    url='https://github.com/kappius/pyheaderfile',
    download_url='https://github.com/kappius/pyheaderfile/archive/%s.tar.gz' %
                 VERSION,
    keywords=['pentaho', 'kettle', 'report', 'ktr', 'kjb', 'xml', 'txt'],
    license='Apache',
    include_package_data=True,
    install_requires=['xlrd', 'xlwt', 'openpyxl', 'unicodecsv'],
    classifiers=['Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Operating System :: OS Independent',
                 'Topic :: Database',
                 'Topic :: Office/Business',
                 'Topic :: Software Development :: Libraries :: '
                 'Python Modules',
                 'Topic :: Utilities'],
)
