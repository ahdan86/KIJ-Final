import DES
import binascii
import secrets

class CBC:
  def __init__(self):
    pass

  def encrypt(self, plaintext, key):
    # Jika panjang plaintext tidak habis dibagi 8(bukan kelipatan 64-bit)
    # maka tambahkan 0 (padding) di belakang plaintext
    if(len(plaintext) % 8 != 0):
      plaintext += "0" * (8 - len(plaintext) % 8)
    
    #Ubah plaintext dan key ke dalam bentuk hex
    plaintext = binascii.hexlify(plaintext.encode('utf-8'))
    key = binascii.hexlify(key.encode('utf-8'))
    
    # Buat 64-bit block dari plaintext    
    plaintext = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]

    # Operasi enkripsi CBC
    # Step (1) Buat IV (Initialization Vector) dengan panjang 64-bit
    IV = self.generateIV()

    # Step(2) Lakukan Operasi DES-CBC
    ciphertext = []
    desFunction = DES.DES()
    key = self.hexToBinary(key.decode('utf-8'), 64)
    for i in range(len(plaintext)):
      
      # ================== BUAT DEBUG YGY ==================
      # print(bin(int(plaintext[i], 16)))
      # print(self.hexToBinary(plaintext[i].decode('utf-8')))
      # print(self.hexToBinary(plaintext[i]))
      # print(IV)
      # print(self.hexToBinary(IV))

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
    print((ciphertext[0]))

  def generateIV(self):
    return secrets.token_hex(8)

  def hexToBinary(self, hex, bit):
    return bin(int(hex, 16))[2:].zfill(bit)

  def decToBinary(self, dec, bit):
    return bin(dec)[2:].zfill(bit)
  