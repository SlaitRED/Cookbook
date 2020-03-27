# 1 The .encode method of a string gives you bytes, and the .decode method of bytes give you a string.
# 2 Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

import base64
from binascii import unhexlify

hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print("hex:", hex_str)

# hex_str binary representation:
print("bin:", bin(int(hex_str, 16))[2:].zfill(8))


def hex_str_to_base64(hex_str):
    byte_seq = unhexlify(hex_str)
    return base64.b64encode(byte_seq)


print("base64:", hex_str_to_base64(hex_str))

# Utf-8 (default):
byte_rep = bytes.fromhex(hex_str)
print("utf-8:", byte_rep)

# Utf-16 representation:
bytelike = hex_str.encode('utf-16')
print("utf-16:", bytelike)
