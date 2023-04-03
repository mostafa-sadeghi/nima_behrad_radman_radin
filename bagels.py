import random

NUM_DIGITS = 3
MAX_GUESSES = 10
spaces = ' ' * 25


def getSecrectNumber():
    numbers = list('0123456789')
    random.shuffle(numbers)
    sec_num = ''
    for i in range(NUM_DIGITS):
        sec_num += numbers[i]
    return sec_num


def getHint(guess, secretNum):
    if guess == secretNum:
        return 'You Got it!'

    hints = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            hints.append('Fermi')
        elif guess[i] in secretNum:
            hints.append('Pico')

    if len(hints) == 0:
        return 'Bagels'
    else:
        return hints


print(f'''{spaces}Bagels Game.
You must guess a {NUM_DIGITS} digits number and you have {MAX_GUESSES} times to win.
When I say:               That means:
    Pico                    One digit is correct but not in the correct spot.
    Fermi                   One digit is correct and in the correct spot.
    Bagel                   No digit is correct.
''')
while True:

    secrectNumber = getSecrectNumber()

    numGuesses = 1
    while numGuesses < MAX_GUESSES:
        guess = ''
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print("You must enter a three digit number.")
            guess = input('> ')

        hints = getHint(guess, secrectNumber)
        print(hints)
        numGuesses += 1
        if guess == secrectNumber:
            break

    print("do you want to play again? (yes or no?)")
    if not input('> ').lower().startswith('y'):
        break
print("thank you for playing")
