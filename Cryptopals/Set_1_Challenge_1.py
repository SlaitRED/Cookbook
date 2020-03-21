# 1 The .encode method of a string gives you bytes, and the .decode method of bytes give you a string.
# 2 Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

import base64
from binascii import unhexlify

hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'


def hex_str_to_base64(hex_str):
    byte_seq = unhexlify(hex_str)
    return base64.b64encode(byte_seq)


print(hex_str_to_base64(hex_str))

# Python is printing in utf-8 by default as below:
byte_rep = bytes.fromhex(hex_str)
print(byte_rep)

# Utf-16 representation
bytelike = hex_str.encode('utf-16')
print(bytelike)
