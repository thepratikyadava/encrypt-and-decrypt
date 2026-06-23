import random
import string
char = " " + string.digits + string.punctuation + string.ascii_letters
char = list(char)
key = char.copy()
random.shuffle(key)

try:
    user_input = input("Tell the message you want to encrpt:-")
    output = ""
    for letter in user_input :
        index = char.index(letter)
        output += key[index]
    print(output)    
except Exception as err:
     print(f"An error found as {err}")

try:
    user_input = input("Tell the message you want to decrypt:-")
    output = ""
    for letter in user_input :
        index = key.index(letter)
        output += char[index]
    print(output)
except Exception as err:
 print(f"An error occured as {err}")

