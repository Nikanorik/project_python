from random import randint
from art_guess import logo
EASY_TURN = 10
HARD_TURN = 5

def check_answer(guess,answer, turns):
    if guess > answer:
        print('You enter number more')
        return turns-1
    elif guess <answer:
        print('You enter number less')
        return turns-1
    else:
        print('You guess!!!')
def set_difficult():
    level = input('Choose a difficult "easy" or "hard":  ')
    print(logo)
    if level=='easy':
        return EASY_TURN
    else:
        return HARD_TURN
def game():
    print('Welcome to the play Guess number')
    print('I thinking number from 1 to 100')
    answer = randint(1,100)

    turns = set_difficult()
    print(f'Amount guess {turns}')
    guess = 0
    while guess!=answer:
        print(f'You have turns attempt {turns}')
        guess = int(input('Enter number: '))
        turns = check_answer(guess,answer,turns)
        if turns==0:
            print('Attempt stop!!!')
            return
game()