#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct


class Encr(object):
    num = int('0933910847463829827159347601486730416058')

    def encrypt(self, password):
        secret = struct.unpack('>%sB' % len(password), bytearray(password))
        s = sum(secret[i] << (i * 8) for i in range(len(password)))
        encrypt = s ^ self.num
        return 'Encrypted %x' % encrypt

    def decrypt(self, password):
        secret = password.split()[1]
        hexa = int(secret, 16)
        encoded = hexa ^ self.num
        return struct.pack("Q", encoded)