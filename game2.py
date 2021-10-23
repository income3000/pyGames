import random
def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_num:
            print('too low')
        if guess > random_num:
            print('too high')
        else :
            print('Ur right')

def comp_guess(x):
    low = 1
    high = x
    feedback = ' '
    while feedback != 'c':
        