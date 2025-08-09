import random
print('*** Generate Random Number ***')

start = int(input('From: '))
end = int(input('To: '))

while True:
    print(f'>>> {random.randint(start, end)}')

    answer = input('Do you want to 1) continue , 2) change the parameters or 3) quit? (1 / 2 / 3): ')
    if answer == '1':
        continue

    elif answer == '2':
        start = int(input('From: '))
        end = int(input('To: '))
        
    elif answer == '3':
        break