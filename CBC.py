import DES
import binascii
import secrets
import Util

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
    key = Util.hexToBinary(key.decode('utf-8'), 64)
    for i in range(len(plaintext)):
      # ================== BUAT DEBUG YGY ==================
      # print(Util.hexToBinary(plaintext[i].decode('utf-8'), 64))
      # print(Util.hexToBinary(IV, 64))
      # ====================================================

      plaintext[i] = Util.hexToBinary(plaintext[i].decode('utf-8'), 64)
      if(i == 0):
        plaintext_xor = int(Util.hexToBinary(IV, 64), 2) ^ int(plaintext[i], 2)
        # print(len(Util.decToBinary(plaintext_xor)))
      else:
        plaintext_xor = int(ciphertext[i-1], 2) ^ int(plaintext[i], 2)
        # print(len(Util.decToBinary(plaintext_xor)))
      ciphertext.append(
          desFunction.encrypt(Util.decToBinary(plaintext_xor, 64), key)
      )
    
    # ciphertext = ''.join(ciphertext)
    # ciphertext = Util.binToHex(ciphertext)
    # print(ciphertext, '('+str(len(ciphertext))+')')
    result = ''
    for i in ciphertext:
      result += Util.binToHex(i)
    print(result)


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
    key = Util.hexToBinary(key.decode('utf-8'), 64)
    for i in range(len(ciphertext)):
      ciphertext[i] = Util.hexToBinary(ciphertext[i], 64)
      resultDES = desFunction.decrypt(ciphertext[i], key)
      if(i==0):
        plaintextXOR = int(Util.hexToBinary(IV, 64), 2) ^ int(resultDES, 2)
      else:
        plaintextXOR = int(ciphertext[i-1], 2) ^ int(resultDES, 2)
      plaintext.append(Util.decToBinary(plaintextXOR, 64))
    
    plaintext = ''.join(plaintext)
    plaintext = Util.binToHex(plaintext)
    # print(plaintext, '('+str(len(plaintext))+')')
    print(Util.hexToPlain(plaintext))

  def generateIV(self):
    return secrets.token_hex(8)