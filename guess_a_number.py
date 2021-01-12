import random

start = int(input('Please enter the start number: '))
end = int(input('Please enter the end number: '))
r = random.randint(start, end)
count = 0
while True:
    count = count + 1
    ask = int(input('Guess a number: '))
    if ask < r:
        print('Guess bigger.')
    elif ask > r:
        print('Guess smaller.')
    else:
        print('Great guess!')
        print('Guess:', count, 'times.')
        break
