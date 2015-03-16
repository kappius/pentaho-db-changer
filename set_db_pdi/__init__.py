#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import ConfigParser
import glob
import os
import warnings
from encr import Encr

CUR_DIR = os.path.dirname(os.path.realpath(__file__))

VERSION = (0, 0, 3)
__version__ = ".".join(map(str, VERSION))


class SetDB(object):
    """ Class to set new database to ktr, kjb and xml files from Pentaho PDI
    and Report Designer.
    """
    def __init__(self, config=os.path.join(CUR_DIR, 'config.ini')):
        """ You can set default configuration file or use default config.ini.
        :param config: configuration file absolute path.
        """
        self.cfg = ConfigParser.ConfigParser(allow_no_value=True)
        self.cfg.read(config)

        self.files = glob.iglob(os.path.join(self.cfg.get('default', 'path'),
                                             "*.*"))

    def write_file_pdi(self, encrypt=True):
        """ Write connection parameters to ktr, kjb and xml files stored in
        path inside default section into configuration file.
        :param encrypt: If you set encrypt False, then it will write password
        without apply pentaho obfuscation (it should be already obfuscated in
        configuration file as explained in README.
        """
        for f in self.files:
            if f.endswith(".xml") or f.endswith(".kjb") or f.endswith(".ktr"):
                tree = ET.parse(f)
                root = tree.getroot()

                for father in root:
                    if father.tag == 'connection':
                        for son in father:
                            try:
                                son.text = self.cfg.get(self.cfg.get('connect',
                                                                     'connect'),
                                                        son.tag)

                            except ConfigParser.NoOptionError:
                                warnings.warn("You didn't set %s -> %s." %
                                              (self.cfg.get('connect',
                                                            'connect'),
                                               son.tag))
                            try:
                                if encrypt and son.tag == 'password':
                                    son.text = Encr().encrypt(son.text)
                            except:
                                raise Exception("Please check if your password"
                                                " is ready to crypt.")

                tree.write(file, encoding='utf-8', xml_declaration=True)
            else:
                warnings.warn("We just support xml, kjb and ktr files. "
                              "%s not supported." % f)


if __name__ == '__main__':
    """ Execute main function when you're not using as a module. """
    try:
        SetDB().write_file_pdi()
        print 'Done'
    except:
        raise