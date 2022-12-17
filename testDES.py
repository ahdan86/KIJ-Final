import DES
import binascii

def hexToBinary(hex, bit):
  return bin(int(hex, 16))[2:].zfill(bit)

def binToHex(bin):
  return hex(int(bin, 2))[2:].zfill(16)

def hexToPlain(hex):
  return (binascii.unhexlify(hex)).decode('ascii')

desFunction = DES.DES()
plaintext = 'AHDAN Ai'
key = '12345678'

plaintext = binascii.hexlify(plaintext.encode('utf-8'))
key = binascii.hexlify(key.encode('utf-8'))
plaintext = hexToBinary(plaintext.decode('utf-8'), 64)
key = hexToBinary(key.decode('utf-8'), 64)

# print(plaintext)
ciphertext = binToHex(desFunction.encrypt(plaintext, key))
print(ciphertext)

ciphertext = hexToBinary(ciphertext, 64)
decrypted = binToHex(desFunction.decrypt(ciphertext, key))
print(hexToPlain(decrypted))

