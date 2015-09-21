#!/usr/bin/python

"""
@author : zryfish
@description : 
"""

import os
import sys

if __name__=="__main__":
    
    hexString1 = "1c0111001f010100061a024b53535009181c"
    hexString2 = "686974207468652062756c6c277320657965"

    if len(sys.argv) == 3:
        hexString1 = sys.argv[1]
        hexString2 = sys.argv[2]

    if len(hexString1) != len(hexString2):
        raise Exception("buffers length is not equal")
        sys.exit(-1)
    print "%x" % (int(hexString1, 16) ^ int(hexString2, 16))

