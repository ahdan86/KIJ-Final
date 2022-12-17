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

    self.PC1 = [57, 49, 41, 33, 25, 17, 9,
                1, 58, 50, 42, 34, 26, 18,
                10, 2, 59, 51, 43, 35, 27,
                19, 11, 3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                7, 62, 54, 46, 38, 30, 22,
                14, 6, 61, 53, 45, 37, 29,
                21, 13, 5, 28, 20, 12, 4]
    
    self.keyShift = [1, 1, 2, 2, 2, 2, 2, 2,
                    1, 2, 2, 2, 2, 2, 2, 1]

    self.PC2 = [14, 17, 11, 24, 1, 5,
                3, 28, 15, 6, 21, 10,
                23, 19, 12, 4, 26, 8,
                16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55,
                30, 40, 51, 45, 33, 48,
                44, 49, 39, 56, 34, 53,
                46, 42, 50, 36, 29, 32]

    self.expansionMatrix = [32, 1, 2, 3, 4, 5,
                            4, 5, 6, 7, 8, 9,
                            8, 9, 10, 11, 12, 13,
                            12, 13, 14, 15, 16, 17,
                            16, 17, 18, 19, 20, 21,
                            20, 21, 22, 23, 24, 25,
                            24, 25, 26, 27, 28, 29,
                            28, 29, 30, 31, 32, 1]
# 
  def encrypt(self, plaintext, key):
    # Proses Encrypt DES
    # Step (1) initial permutation untuk blok 64-bit
    plaintext_ip = self.initPermutation(plaintext)
    # print(plaintext[i])

    # Step (2) Split 64-bit block menjadi 2 bagian 32-bit
    left = plaintext_ip[:32]
    right = plaintext_ip[32:]

    # Step (3) Proses Feistel Cipher
  

  def initPermutation(self, plaintext):
    result = ''
    # change the plaintext to binary
    plaintext = self.hexToBinary(plaintext)
    for i in range(len(self.IP)):
      result += plaintext[self.IP[i]-1]
    return result

  def decToBinary(self, dec):
    return bin(dec)[2:].zfill(64)

  def decrypt(self, plaintext, key):
    # ...
    print("Test Decrypt")
