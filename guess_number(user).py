import random

def guess_number():
    attempt = 0
    low = 1
    high = 100
    number = random.randint(1, 100)

    while True:
        guess = int(input(f"Guess a number between {low} and {high}: "))
        attempt += 1
        if guess == number:
            break
        elif guess < number:
            print('too low')
            low = guess
        elif guess > number:
            print('too high')
            high = guess
        if attempt == 5:
            attempt = -1
            break
        print(f'!! You have {5 - attempt} attempts remaining !!')

    return number, attempt

number, attepmts = guess_number()
if attepmts == -1:
    print(f'You lost! the number was {number}')
else:
    print(f'Congradulations! you guessed {number} by {attepmts} attempts.')