import random

r = random.randint(1, 100)
while True:
    ask = int(input('Guess a number: '))
    if ask < r:
        print('Guess bigger.')
    elif ask > r:
        print('Guess smaller.')
    else:
        print('Great guess!')
        break