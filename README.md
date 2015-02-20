# pentaho-db-changer
Change dynamically Pentaho PDI database connection

How to use
==========

Before execute the program you need to configure .ini file (config.ini) with your database settings.

You can follow this example:

First of all use a section 'connect' to select which database you will use.

[connect]
connect = connect_local

Then, create a default section with the absolute path for pdi files.

[default]
path = /home/pdi

At last, create a section for each connection that you want to use and change easyly.

[conect_server]
server = xxxxxx
username = xxxxxx
password = my_pass

[conect_local]
server = localhost
username = root
password = other_pass

Just execute __init__.py file
