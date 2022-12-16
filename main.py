import CBC
import DES

# take user input and print it
plainText = input("Enter the text to be encrypted: ")
# key = input("Enter the key: ")
key = input("Enter the key (8 characters): ")

# check if the key is valid 64-bit
if len(key) != 8:
  print("Panjang key harus 8 karakter")
  exit()

# call DES function
desFunction = DES.DES()
# encrypt the plaintext
desFunction.encrypt(plainText, key)
