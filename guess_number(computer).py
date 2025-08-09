import random

def guess_number():
    low = 0
    high = 100
    attempts = 0
    while True:
        guess = random.randint(low, high)
        attempts += 1
        answer = input(f'Computer guessed {guess}, is it correct, low or high? (c / l / h):  ')
        if answer == 'c':
            break
        elif answer == 'l':
            low = guess + 1
        elif answer == 'h':
            high = guess - 1
        if attempts == 5:
            attempts = -1
            break

    return guess, attempts

number, attempts = guess_number()
if attempts == -1:
    print('Computer lost!')
else:
    print(f'Computer guessed {number} in {attempts} attempts.')
