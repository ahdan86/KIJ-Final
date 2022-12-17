import MatrixCollection
class DES:
  def __init__(self):
    self.matrixCollection = MatrixCollection.MatrixCollection()
    self.roundKey = []
# 
  def encrypt(self, plaintext, key):
    # Proses Encrypt DES
    # Step (1) initial permutation untuk blok 64-bit
    plaintext_ip = self.initPermutation(plaintext)
    # print(plaintext_ip)

    # Step (2) Split 64-bit block menjadi 2 bagian 32-bit
    left = plaintext_ip[:32]
    right = plaintext_ip[32:]
    # print(left)
    # print(right)

    # Step (3) Proses Feistel Cipher
    # Step (3.1) Generate Round Key
    for i in range(0, 16):
      if(i == 0):
        cKey, dKey = self.generateRoundKeyPC1(key)
      # Leftshift CKey dan DKey
      keyShift = getattr(self.matrixCollection, 'keyShift')
      cKey = cKey[keyShift[i]:] + cKey[:keyShift[i]]
      dKey = dKey[keyShift[i]:] + dKey[:keyShift[i]]
      # Gabungkan CKey dan DKey lalu permutasi PC-2
      newKey = cKey + dKey
      newKey = self.generateRoundKeyPC2(newKey)
      self.roundKey.append(newKey)

    print(self.roundKey)
  
  def initPermutation(self, plaintext):
    IP = getattr(self.matrixCollection, 'IP')
    result = ''
    for i in range(len(IP)):
      result += plaintext[IP[i]-1]
    return result

  def generateRoundKeyPC1(self, key):
    # Permutasi PC-1
    PC1 = getattr(self.matrixCollection, 'PC1')
    cKey = ''
    dKey = ''
    for i in range(len(PC1)):
      if(i<28):
        cKey += key[PC1[i]-1]
      else:
        dKey += key[PC1[i]-2]
    return cKey, dKey

  def generateRoundKeyPC2(self, key):
    # Permutasi PC-2
    PC2 = getattr(self.matrixCollection, 'PC2')
    result = ''
    for i in range(len(PC2)):
      result += key[PC2[i]-1]
    return result

  def decToBinary(self, dec):
    return bin(dec)[2:].zfill(64)

  def decrypt(self, plaintext, key):
    # ...
    print("Test Decrypt")
