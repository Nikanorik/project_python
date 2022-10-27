import random


def main():
    vocabulary = {'step by step': 'шаг за шагом', 'arrive': 'прибывать', 'join': 'присоединиться', 'soon': 'ближайший',
                  'the entrance exams': 'вступительные экзамены', 'take driving lessons': 'брать уроки вождения',
                  'advice': 'совет', 'be on time': 'будь вовремя', 'simple': 'простое', 'compaund': 'составное',
                  'carry': 'нести', 'still': 'все еще', 'lie': 'лежать', 'break': 'перерыв', 'tidy up': 'прибраться',
                  'A yong man is standing at the window': 'молодой мужчина стоит у окна', 'paint': 'красить',
                  'neighbors': 'соседи', 'sink': 'раковина', 'where am I': 'где я?',
                  'is he from USA': 'Он из Америки?', 'how old are you': 'сколько тебе лет?', 'ceiling': 'потолок',
                  'next time': 'следующий раз', 'take an english exam': ' сдавать английский экзамен',
                  'do makeovers': 'делать ремонт', 'feed the cat': 'кормить кота',
                  'enter the university': 'поступать в университет', 'stay at home': 'оставаться дома',
                  'how will you get visa': 'как ты будешь получать визу?',
                  'take english classes': 'брать уроки английского языка', 'tell the truth': 'говорить правду',
                  'invite': 'пригласить', 'organize a party': 'устраивать вечеринку',
                  'repair the computer': 'чинить компьютер', 'solve the problem': 'решить проблему',
                  'take an exam': 'сдавать экзамен', 'truth': 'правда', 'the day after tomorrow': 'послезавтра',
                  'how many classes will you have tomorrow': 'как много уроков ты имеешь завтра?',
                  'i study well at school': 'я учусь хорошо в школе', 'let is talk': 'позволь нам поговорить',
                  'make a present': 'делать подарки', 'be married': 'быть замужем',
                  'groccery store': 'продуктовый магазин', 'give present': 'дарить подарки',
                  'brush teeth': 'чистить зубы', 'take a shower': 'принимать душ', 'film videos': 'делать видео',
                  'run in the forest': 'бегать в лесу', 'why are you at home': 'почему ты дома?', 'dirty': 'грязный',
                  'single': 'одинокий', 'where are you from': 'откуда ты?', 'there': 'там', 'i am out': 'я на руже'}
    flag = True
    check_plus = 0
    check_minus = 0
    while flag:
        i = random.randint(0, len(vocabulary) - 1)
        answ_one = list(vocabulary)[i]
        print(vocabulary[answ_one])
        answer = input('Enter answer: ')

        if answer == answ_one:
            print('It is right!!!')
            check_plus += 1
            new_answer = input('Will you next?(y/n): ')
            if new_answer != 'y':
                flag = False
        else:
            check_minus -= 1
            print('Wrong!!!')
            print(f'Right answer: {answ_one}')
            new_answer = input('Will you next?(y/n): ')
            if new_answer != 'y':
                flag = False

    print(f'Thank you!!! Plus: {check_plus}, Minus: {check_minus}')


if __name__ == '__main__':
    main()
