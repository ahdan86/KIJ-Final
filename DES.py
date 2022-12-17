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
    # print(len(left), len(right))

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
    # print(self.roundKey)

    # Step(3.2) Proses Inti Feistel
    for i in range (0,16):
      resultF = self.fungsiF(right, self.roundKey[i])
      leftXOR = int(left, 2) ^ int(resultF, 2)
      # print("=======")
      # print(resultF)
      # print(left)
      # print(self.decToBinary(leftXOR, 32))
      # print("=======")
      left = right
      right = self.decToBinary(leftXOR, 32)
    
    # Step(4) Inverse Initial Permutation
    leftRight = left + right
    ciphertext = self.inverseInitPermutation(leftRight)
    return ciphertext

  
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

  def fungsiF(self, block, key):
    # Ekspansi block menjadi 48 bit
    newBlock = ''
    expansionMatrix = getattr(self.matrixCollection, 'expansionMatrix')
    for i in range(len(expansionMatrix)):
      newBlock += block[expansionMatrix[i]-1]

    # Operasi XOR dengan key-i
    newBlock = int(newBlock, 2) ^ int(key, 2)
    newBlock = self.decToBinary(newBlock, 48)

    # Buat 6-bit block dari newBlock dan dilakukan subtitusi S-box
    newBlock = [newBlock[i:i+6] for i in range(0, len(newBlock), 6)]
    for i in range(0, 8):
      index = 'S'+str(i+1)
      sbox = getattr(self.matrixCollection, index)
      outerBit = int(newBlock[i][0] + newBlock[i][5], 2)
      innerBit = int(newBlock[i][1:5], 2)
      newBlock[i] = self.decToBinary(sbox[outerBit][innerBit], 4)
    newBlock = ''.join(newBlock)

    # Permutasi P-box
    pbox = getattr(self.matrixCollection, 'p_Box')
    result = ''
    for i in range(len(pbox)):
      result += newBlock[pbox[i]-1]
    return result

  def inverseInitPermutation(self, block):
    IPinverse = getattr(self.matrixCollection, 'IPinverse')
    result = ''
    for i in range(len(IPinverse)):
      result += block
    return result  

  def decToBinary(self, dec, bit):
    return bin(dec)[2:].zfill(bit)

  def decrypt(self, plaintext, key):
    # ...
    print("Test Decrypt")
  