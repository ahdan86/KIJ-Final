import CBC
import DES

# Take user input for choose mode:
mode = input("Pilih E (Encrypt) / D (Decrypt): ")
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
