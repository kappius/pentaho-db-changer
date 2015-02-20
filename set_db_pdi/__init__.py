#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import ConfigParser
import glob

cfg = ConfigParser.ConfigParser(allow_no_value=True)
cfg.read('config.ini')

arquivos = glob.glob(cfg.get('default', 'path') + "/*.k*")


for arquivo in arquivos:
    tree = ET.parse(arquivo)
    root = tree.getroot()

    for pai in root:
        if pai.tag == 'connection':
            for filho in pai:
                try:
                    filho.text = cfg.get(cfg.get('conect', 'conect'),
                                         filho.tag)
                except ConfigParser.NoOptionError:
                    pass
    tree.write(arquivo, encoding='utf-8', xml_declaration=True)

