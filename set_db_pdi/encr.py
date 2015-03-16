#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii


class Encr(object):
    """ Cryptography class used to obfuscate passwords in Pentaho PDI.
    New Report Designer cryptography is not working, but PDI still with this
    approach: http://goo.gl/ukhXY2

    Report designer fixed here: http://jira.pentaho.com/browse/PRD-3608
    """
    num = int('0933910847463829827159347601486730416058')

    def encrypt(self, password):
        """ Encrypt passwords with PDI obfuscation following this file:
        http://goo.gl/zXWHjg
        :param password: Password to be obfuscated
        :return: Encrypted format for Pentaho
        """
        secret = int(binascii.hexlify(password), 16)
        encrypt = secret ^ self.num
        return 'Encrypted %x' % encrypt

    def decrypt(self, password):
        """ Receives encrypted password and decrypt it.
        :param password: Obfuscated password
        :return: decrypted password human readable
        """
        hexa = password.split()[1]
        secret = int(hexa, 16)
        encoded = secret ^ self.num
        return binascii.unhexlify("%x" % encoded)