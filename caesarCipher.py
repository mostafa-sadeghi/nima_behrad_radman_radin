# name = "mehrad"
# key = 2

# char_number = ord('m')
# print(char_number)
# char_number += key
# print(chr(char_number))

# for char in name:
#     char_number = ord(char) + key
#     print(chr(char_number), end='')
# print()
# for char in 'ogjtcf':
#     char_number = ord(char) - key
#     print(chr(char_number), end='')
import string
SYMBOLS = string.ascii_uppercase
# print(SYMBOLS)
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt? ')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

while True:
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key (0 to {maxKey}) to use')
    response = input('> ')
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print(f'Enter the message to {mode}')
message = input('> ').upper()

translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)
        translated += SYMBOLS[num]
    else:
        translated += symbol
print(translated)
