import random
import string
char = " " + string.digits + string.punctuation + string.ascii_letters
char  = list(char)
key = char.copy()
random.seed(42)
random.shuffle(key)
k = len(char)
def encrypt():
  try:
    user_input = input("Tell the message you want to encrpt:-")
    output = ""
    for letter in user_input :
        index = char.index(letter)
        output += key[index]
    print(output)    
  except Exception as err:
     print(f"An error found as {err}")

def decrypt():
    user_input = input("Tell the message you want to decrypt:-")
    output = ""
    for letter in user_input :
        index = key.index(letter)
        output += char[index]
    print(output)


a = int(input("Tell the operation you want to perform for encryption enter 1 and for decryption enter 2:-"))
if a == 1 :
   encrypt()
else:
   decrypt()