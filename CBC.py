import DES
import binascii
import secrets

class CBC:
  def __init__(self):
    pass

  def encrypt(self, plaintext, key):
    #Ubah plaintext dan key ke dalam bentuk hex
    plaintext = binascii.hexlify(plaintext.encode('utf-8'))

    # tambahkan padding jika panjang plaintext kurang dari 64-bit
    if(len(plaintext) % 16 != 0):
      padding = 16 - (len(plaintext) % 16)
      plaintext += b'0' * padding

    key = binascii.hexlify(key.encode('utf-8'))
    
    # Buat 64-bit block dari plaintext    
    plaintext = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]

    # Operasi enkripsi CBC
    # Step (1) Buat IV (Initialization Vector) dengan panjang 64-bit
    # IV = self.generateIV()
    IV = "12345678"
    IV = binascii.hexlify(IV.encode('utf-8'))

    # Step(2) Lakukan Operasi DES-CBC
    ciphertext = []
    desFunction = DES.DES()
    key = self.hexToBinary(key.decode('utf-8'), 64)
    for i in range(len(plaintext)):
      # ================== BUAT DEBUG YGY ==================
      # print(self.hexToBinary(plaintext[i].decode('utf-8'), 64))
      # print(self.hexToBinary(IV, 64))
      # ====================================================

      plaintext[i] = self.hexToBinary(plaintext[i].decode('utf-8'), 64)
      if(i == 0):
        plaintext_xor = int(self.hexToBinary(IV, 64), 2) ^ int(plaintext[i], 2)
        # print(len(self.decToBinary(plaintext_xor)))
      else:
        plaintext_xor = int(ciphertext[i-1], 2) ^ int(plaintext[i], 2)
        # print(len(self.decToBinary(plaintext_xor)))
      ciphertext.append(
          desFunction.encrypt(self.decToBinary(plaintext_xor, 64), key)
      )
    
    # ciphertext = ''.join(ciphertext)
    # ciphertext = self.binToHex(ciphertext)
    # print(ciphertext, '('+str(len(ciphertext))+')')
    result = ''
    for i in ciphertext:
      print(i)
      result += self.binToHex(i)
    print(result, '('+str(len(result))+')')


  def decrypt(self, ciphertext, key):
    key = binascii.hexlify(key.encode('utf-8'))

    # Buat 64-bit block dari ciphertext    
    ciphertext = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]

    # Step (1) Buat IV (Initialization Vector) dengan panjang 64-bit
    # IV = self.generateIV()
    IV = "12345678"
    IV = binascii.hexlify(IV.encode('utf-8'))

    # Step(2) Lakukan Operasi DES-CBC
    plaintext = []
    desFunction = DES.DES()
    key = self.hexToBinary(key.decode('utf-8'), 64)
    for i in range(len(ciphertext)):
      ciphertext[i] = self.hexToBinary(ciphertext[i], 64)
      resultDES = desFunction.decrypt(ciphertext[i], key)
      if(i==0):
        plaintextXOR = int(self.hexToBinary(IV, 64), 2) ^ int(resultDES, 2)
      else:
        plaintextXOR = int(ciphertext[i-1], 2) ^ int(resultDES, 2)
      plaintext.append(self.decToBinary(plaintextXOR, 64))
    
    plaintext = ''.join(plaintext)
    plaintext = self.binToHex(plaintext)
    print(plaintext, '('+str(len(plaintext))+')')
    print(self.hexToPlain(plaintext))

  def generateIV(self):
    return secrets.token_hex(8)

  def hexToBinary(self, hex, bit):
    return bin(int(hex, 16))[2:].zfill(bit)

  def decToBinary(self, dec, bit):
    return bin(dec)[2:].zfill(bit)

  def binToHex(self, bin):
    return hex(int(bin, 2))[2:].zfill(16)

  def hexToPlain(self, hex):
    return (binascii.unhexlify(hex)).decode('ascii')
  