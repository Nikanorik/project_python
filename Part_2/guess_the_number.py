import random

from art_guess import logo

print('Welcom in my game is name GUESS THE NUMBER')
print('Number from 1 to 100')
level = input('Enter level "easy" or "hard": ')
print(logo)
computer = random.randint(1, 101)


def comparison(num, computer):
    if num == computer:
        print('You guessed!!!!')
    elif num > computer:
        print('Your number more!')
    elif num < computer:
        print('Your number less!!!')


def while_number(i):
    flag = True
    while flag:
        print(f'Attempt number {i}')
        number = int(input('Enter number: '))
        comparison(number, computer)
        if computer == number:
            return 10
        else:
            return 0
def level_enter(level):
    if level == 'easy':
        print('You have 10 attempt')
        i = 1
        while i <= 10:
            i += 1 + while_number(i)
    elif level == 'hard':
        print('You have 5 attempt')
        i = 1
        while i <= 5:
            i += 1 + while_number(i)
    else:
        print('Error. Choose level "hard" or "easy"')


level_enter(level)
