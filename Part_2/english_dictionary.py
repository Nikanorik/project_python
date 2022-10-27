import random
def main():
    vocabulary = {'step by step':'шаг за шагом', 'arrive':'прибывать', 'join':'присоединиться'}
    flag = True
    while flag:
        i= random.randint(0,len(vocabulary)-1)
        answ_one=list(vocabulary)[i]
        print(vocabulary[answ_one])
        answer = input('Enter answer: ')
        if answer == answ_one:
            print('It is right!!!')
            new_answer = input('Will you next?(y/n): ')
            if new_answer != 'y':
                flag = False
        else:
            print('Wrong!!!')
            print(f'Right answer: {answ_one}')
            new_answer = input('Will you next?(y/n): ')
            if new_answer != 'y':
                flag = False
    print('Thank you!!')
if __name__ == '__main__':
    main()
