import random
import string
char = " " + string.digits + string.punctuation + string.ascii_letters
print(char)
char  = list(char)
print(type(char))
key = char.copy()
random.shuffle(key)
print(key)
k = len(char)
print(k)