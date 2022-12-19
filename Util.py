import binascii

def hexToBinary(hex, length):
  return bin(int(hex, 16))[2:].zfill(length)

def decToBinary(dec, length):
  return bin(dec)[2:].zfill(length)
  
def binToHex(bin):
  return hex(int(bin, 2))[2:].zfill(16)

def hexToPlain(hex):
  return (binascii.unhexlify(hex)).decode('ascii')

def plainToHex(plain):
  return binascii.hexlify(plain.encode('utf-8'))