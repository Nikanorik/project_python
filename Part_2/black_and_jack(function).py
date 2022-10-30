import random
from art_bj import logo

def deal_card():
    '''Return a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw!!!'
    elif user_score == 0:
        return 'You win!!! You have blackjack!'
    elif computer_score == 0:
        return 'You Lose!!! Computer have blackjack!'
    elif user_score > 21:
        return 'You Lose!'
    elif computer_score > 21:
        return 'Comp Lose!'
    elif user_score > computer_score:
        return 'You win!!!'
    else:
        return 'Computer Win!!!'
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards next: {user_cards} and score: {user_score}')
        print(f'First card computer: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input('Type "y" to get another card, type "n" to pass: ')
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(
        f'Final hand user: {user_cards} and score : {user_score}; '
        f'final hand computer: {computer_cards} and score: {computer_score}')
    print(compare(user_score,computer_score))
while input('You want to game in blackjack?(y/n): '):
    play_game()
print('Thank you!')
