import CBC
import DES
from SHA512 import SHA512

# Take user input for choose mode:
mode = input("Pilih A (DES-CBC) / B (SHA-512): ")
mode = mode.upper()
if mode == 'A':
  mode = input("Pilih E (Encrypt) / D (Decrypt): ")
  mode = mode.upper()
  if mode != 'E' and mode != 'D':
    print("Pilihan tidak valid")
    exit()
  # buat instance CBC
  cbc = CBC.CBC()
  if(mode == 'E'):
    # Take User Input For Plaintext
    plaintext = input("Enter the text to be encrypted: ")
    # Take User Input For Key
    key = input("Enter the key (8 characters): ")
    # check if the key is valid 64-bit
    if len(key) != 8:
      print("Panjang key harus 8 karakter")
      exit()        
    cbc.encrypt(plaintext, key) 

  elif(mode == 'D'):
    # Take User Input For CipherText
    ciphertext = input("Enter the text to be decrypted: ")
    # Take User Input For Key
    key = input("Enter the key (8 characters): ")
    # check if the key is valid 64-bit
    if len(key) != 8:
      print("Panjang key harus 8 karakter")
      exit()        
    cbc.decrypt(ciphertext, key) 

elif mode == 'B':
  # Dapetin user input
  plaintext = input("Masukkan text yang mau dihash: ")
  # Buat instance SHA512
  sha512 = SHA512()
  # Hash plaintext
  hash = sha512.hash(plaintext)
  print(hash)
