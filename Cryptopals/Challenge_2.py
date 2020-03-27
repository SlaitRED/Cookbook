
from binascii import unhexlify
from binascii import hexlify


hex_a = "1c0111001f010100061a024b53535009181c"
hex_b = "686974207468652062756c6c277320657965"

print(hex_a)
print(hex_b)

int_a = unhexlify(hex_a)
int_b = unhexlify(hex_b)


scale = 16
num_of_bits = 8

bin_a = bin(int(hex_a, scale))[2:].zfill(num_of_bits)
bin_b = bin(int(hex_b, scale))[2:].zfill(num_of_bits)

print(bin_a)
print(bin_b)

res = int(bin_a) ^ int(bin_b)
print(res)

print(hex(res))