import random

choices = ["rock", "paper", "scissors"]

def winer(user, computer):
    status = ''
    if user == 'r':
        if computer == 'scissors':
            status = 'user'
        elif computer == 'paper':
            status = 'computer'
        elif computer == 'rock':
            status = 'tie'

    elif user == 'p':
        if computer == 'scissors':
            status = 'computer'
        elif computer == 'paper':
            status = 'tie'
        elif computer == 'rock':
            status = 'user'

    elif user == 's':
        if computer == 'scissors':
            status = 'tie'
        elif computer == 'paper':
            status = 'user'
        elif computer == 'rock':
            status = 'computer'

    return status



def play():
    user = input('Rock Paper Scissors?(r / p / s):  \n').lower()
    computer = random.choice(choices)
    print(computer)
    status = winer(user, computer)
    if status == 'user':
        print(f'Congratulations! You won!')
    elif status == 'computer':
        print(f'Sorry , you lost!')
    elif status == 'tie':
        print("It's a tie!")

play()
while True:
    order = input('You wanna play again? (y / n): ').lower() == 'y'
    if order:
        play()
        continue




