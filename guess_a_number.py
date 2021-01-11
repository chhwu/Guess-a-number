import random

r = random.randint(1, 100)
count = 0
while True:
    ask = int(input('Guess a number: '))
    count = count + 1
    if ask < r:
        print('Guess bigger.')
    elif ask > r:
        print('Guess smaller.')
    else:
        print('Great guess!')
        print('Guess:', count, 'times.')
        break
