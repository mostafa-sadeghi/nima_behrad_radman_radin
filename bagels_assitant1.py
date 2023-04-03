import random

RANK = ['ones', 'tens', 'hundreds']

digits = [0]*3

def generate_random_number():
    number = random.randint(100,999)
    i = 0
    while number != 0:
        print(RANK[i],number % 10)
        digits.pop((3-i-1))
        digits.insert((3-i-1),number % 10)
        number //= 10  # number = number // 10
        i += 1

    
    if len(digits) != len(set(digits)):
        generate_random_number()
    return digits

print(generate_random_number())