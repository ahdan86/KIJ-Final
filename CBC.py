import DES
import binascii
import os

class CBC:
  def __init__(self):
    pass

  def encrypt(self, plaintext, key):
    # Jika panjang plaitext tidak habis dibagi 8(bukan kelipatan 64-bit)
    # maka tambahkan 0 (padding) di belakang plaintext
    if(len(plaintext) % 8 != 0):
      plaintext += "0" * (8 - len(plaintext) % 8)
    
    plaintext = binascii.hexlify(plaintext.encode('utf-8'))

    # buat 64-bit block dari plaintext    
    plaintext = [plaintext[i:i+4] for i in range(0, len(plaintext), 4)]

  def stringToBinary(self, string):
    return ''.join(format(ord(i), '08b') for i in string)

  def generateIV(self):
    return os.urandom(8)

  def hexToBinary(self, hex):
    return bin(int(hex, 16))[2:].zfill(64)