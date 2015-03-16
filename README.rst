Pentaho DB Changer
******************

Change dynamically Pentaho database connections from kjb, ktr and xml files

Installation
============

::

    pip install pentaho-db-changer


How to Use
==========

Before execute the program you need to configure .ini file (config.ini) with your database settings.

You can follow this example:

First of all use a section 'connect' to select which database you will use.

[connect]
connect = connect_local

Then, create a default section with the absolute path for pdi files.

[default]
path = /home/pdi

At last, create a section for each connection that you want to use and change easily.

[conect_server]
server = xxxxxx
username = xxxxxx
password = my_pass

[conect_local]
server = localhost
username = root
password = other_pass

Just execute \__init__.py file as follow:
    
    cd set_db_pdi
    python __init__.py

Using as a Module
=================

Download this project with:

::

    git clone https://github.com/kappius/pentaho-db-changer.git

All modules are in **set_db_pdi** folder and you can copy this folder and put inside your modules folder.

Then, import using:

::

    from set_db_pdi import SetDB

You can set a custom configuration file name using:

::

    SetDB('settings.ini').write_file_pdi()
    

If your password is encrypted (using right pdi format), then call:

::

    SetDB().write_file_pdi(encrypt=False)

If not, then:

::

    SetDB().write_file_pdi() # this is default call when you execute __init__.py file

You know if it is encrypted if password in config.ini is in format:

::

    password = Encrypted 1ad32da2de2da7886

Using in reports
================

It works with Pentaho Report Designer's files (.prpt) too, but only using 
**encrypt=False** since this issue was solved: http://jira.pentaho.com/browse/PRD-3608

Just unzip .prpt files and get file datasources\sql-ds.xml

This file (sql-ds.xml) is like .kjb and .ktr files and use same connection names.
