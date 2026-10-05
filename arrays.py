from array import array
arry = [1,2,3,4,5,6,7,8,]
val = array('i', arry) 

str = 1
try:
  print(val.index(str))
except NameError,TypeError,ValueError:
  print('Value not found in array!')


# English letter
print(len("A".encode('utf-8')))  # 1 byte (8 bits)

# Telugu letter
print(len("అ".encode('utf-8')))  # 3 bytes (24 bits)

# Emoji
print(len("🔥".encode('utf-8')))  # 4 bytes (32 bits)


import struct

def print_float_bits(number):
  packed_bytes = struct.pack('d', number)
  raw_int = struct.unpack('Q',packed_bytes)[0]

  binary_str = f"{raw_int:064b}"

  sign = binary_str[0]
  exponent = binary_str[1:12]
  mantissa = binary_str[12:]
  print(f'Packed bits: {packed_bytes}')
  print(f'Raw int: {raw_int}')
  print(f'Number: {number}')
  print(f'Sign bit (1 bit): {sign}')
  print(f'Exponent (11 bits): {exponent}')
  print(f'mantissa (52 bits): {mantissa}')
  print(f'Full 64-bit Binary: {binary_str}\n')

print_float_bits(5.75)
print_float_bits(-0.223)