# random password genrator:√√√
import string
import random
import pyperclip

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

plen = int(input('Enter your password length:\n'))

s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

# print(s)
random.shuffle(s)
# print(s)   # shuffle list
print(''.join(s[0:plen]))
pyperclip.copy(''.join(s[0:plen]))
pyperclip.paste()

print('*')
print('*')
print('*')
print('*')
print('*')


 
# pyperclip.copy('The text to be copied to the clipboard.')
# print(pyperclip.paste())
# 'The text to be copied to the clipboard.'