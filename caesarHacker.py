import string
SYMBOLS = string.ascii_uppercase


def show_balance(login_result):
    if login_result:
        print("Login Success")
        print("Welcome Your profile page")
        if input('> Do you want to check your balance(yes or no)? ').lower().startswith('y'):
            print("money:", "10000000000000000000000000000000000000000")
    else:
        print("permission denied!!!!")


def login(password, key=5):
    translated = ''
    for symbol in password:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key
            if num < 0:
                num += len(SYMBOLS)
            translated += SYMBOLS[num]
        else:
            translated += symbol
    return translated == "NIMA123"


# user_token = input('Enter token to login: ')
# login_result = login(user_token)
# show_balance(login_result)
