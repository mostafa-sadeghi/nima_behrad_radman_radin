import string
from caesarHacker import login, show_balance
SYMBOLS = string.ascii_uppercase
message = input('> ')
all_tokens = []
for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num + key
            if num >= len(SYMBOLS):
                num = num - len(SYMBOLS)

            translated += SYMBOLS[num]

        else:
            translated += symbol
        all_tokens.append(translated)
# print(all_tokens)
status = False
for token in all_tokens:
    if login(token):
        status = True
        print("token cracked!!!")
        show_balance(token)
        break
if not status:
    print("token was not valid!!!!")
