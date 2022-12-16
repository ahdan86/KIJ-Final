import binascii
class DES:
  def __init__(self):
    # matriks untuk IP (Initial Permutation)
    self.IP =  [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

  
  def encrypt(self, plaintext, key):
    # Proses Encrypt DES
    # Step (1) initial permutation untuk tiap 64-bit block
    for i in range(len(plaintext)):
      plaintext[i] = self.initPermutation(plaintext[i])
      print(plaintext[i])

    # Step (2) Split 64-bit block menjadi 2 bagian 32-bit
    # Step (3) Proses Feistel Cipher
  

  def initPermutation(self, plaintext):
    result = ''
    # change the plaintext to binary
    plaintext = self.hexToBinary(plaintext)
    for i in range(len(self.IP)):
      result += plaintext[self.IP[i]-1]
    return result

  def stringToBinary(self, string):
    return ''.join(format(ord(i), '08b') for i in string)

  def hexToBinary(self, hex):
    return bin(int(hex, 16))[2:].zfill(64)

  def decrypt(self, plaintext, key):
    # ...
    print("Test Decrypt")
