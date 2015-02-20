#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import ConfigParser
import glob
from encr import Encr


class SetDB(object):
    def __init__(self):
        self.cfg = ConfigParser.ConfigParser(allow_no_value=True)
        self.cfg.read('config.ini')

        self.files = glob.glob(self.cfg.get('default', 'path') + "/*.k*")

    def write_file_pdi(self):
        for file in self.files:
            tree = ET.parse(file)
            root = tree.getroot()

            for father in root:
                if father.tag == 'connection':
                    for son in father:
                        try:
                            if son.tag == 'password':
                                son.text = Encr().encrypt(self.cfg.get(
                                    self.cfg.get('connect', 'connect'),
                                    son.tag))

                            else:
                                son.text = self.cfg.get(
                                    self.cfg.get('connect',
                                                 'connect'),
                                    son.tag)
                        except ConfigParser.NoOptionError:
                            pass

            tree.write(file, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    SetDB().write_file_pdi()