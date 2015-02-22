#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct


class Encr(object):
    """ Cryptography class used to obfuscate passwords in Pentaho PDI.
    New Report Designer cryptography is not working, but PDI still with this
    approach: https://github.com/pentaho/pentaho-kettle/blob/master/core/src/org/pentaho/di/core/encryption/Encr.java

    Report designer fixed here: http://jira.pentaho.com/browse/PRD-3608
    """
    num = int('0933910847463829827159347601486730416058')

    def encrypt(self, password):
        """ Encrypt passwords with PDI obfuscation following this file:
        https://github.com/pentaho/pentaho-kettle/blob/master/core/src/org/pentaho/di/core/encryption/KettleTwoWayPasswordEncoder.java
        :param password: Password to be obfuscated
        :return: Encrypted format for Pentaho
        """
        secret = struct.unpack('>%sB' % len(password), bytearray(password))
        s = sum(secret[i] << (i * 8) for i in range(len(password)))
        encrypt = s ^ self.num
        return 'Encrypted %x' % encrypt

    def decrypt(self, password):
        """ Receives encrypted password and decrypt it.
        :param password: Obfuscated password
        :return: decrypted password human readable
        """
        # TODO not working with more and less than 8 characters passwords
        secret = password.split()[1]
        hexa = int(secret, 16)
        encoded = hexa ^ self.num
        return struct.pack("Q", encoded)