import random

from art_bj import logo

def main():
    flag = input('Do you want to play a blackjack?(y/n): ')
    while flag == 'y':
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        list_user = []
        list_comp = []
        for i in range(2):
            card_user = random.choice(cards)
            card_comp = random.choice(cards)
            list_comp.append(card_comp)
            list_user.append(card_user)
        print(f'cards user: {list_user}')
        print(f'first card comp: {list_comp[0]}')
        sum_user = sum(list_user)
        sum_comp = sum(list_comp)
        if (sum_user > 21) and (11 in list_user):
            sum_user -= 10
        if (sum_comp > 21) and (11 in list_comp):
            sum_comp -= 10

        flag2 = input('Do you want give card?(y/n): ')
        while flag2 == 'y':
            card_user = random.choice(cards)
            list_user.append(card_user)
            sum_user += card_user
            print(f'cards user: {list_user}')
            print(f'first card comp: {list_comp[0]}')
            if sum_user <= 21:
                flag2 = input('Do you want more card?(y/n): ')
            else:
                print(f'user Enumeration: {list_user}, score:{sum_user}. Winner comp {list_comp}, score:{sum_comp}!!!')
                flag2 = 'n'
        flag3 = True
        while flag3:
            if sum_comp < 17:
                card_comp = random.choice(cards)
                list_comp.append(card_comp)
                sum_comp += card_comp
            else:
                flag3 = False


        if sum_comp <= 21 and sum_user<21 and sum_user < sum_comp:
            print(f'Winner comp, cards user: {list_user}, score:{sum_user}; cards comp : {list_comp}, score:{sum_comp}')
        elif sum_comp <= 21 and sum_user<=21 and sum_user == sum_comp:
            print(f'DRAW!!! cards user: {list_user}, score:{sum_user}; cards comp : {list_comp}, score:{sum_comp}')
        elif sum_comp < 21 and sum_user <= 21 and sum_comp < sum_user:
            print(f'Winner user, cards user: {list_user}, score:{sum_user}; cards comp : {list_comp}, score:{sum_comp}')
        elif sum_comp > 21 and sum_user<=21:
            print(f'comp Enumeration: {list_comp},score:{sum_comp}. Winner user {list_user}, score:{sum_user}!!!')
        flag = input('Do you want more to play a blackjack?(y/n): ')

    print('Thank you!')
if __name__ == '__main__':
    main()
