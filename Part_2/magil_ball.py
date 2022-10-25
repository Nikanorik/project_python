import random


def main():
    file_new = open('8_ball_responses.txt','r')
    list_one = []
    for i in file_new:
        i=i.rstrip('\n')
        list_one.append(i)
    search = input('Enter question with answer yes or no: ')
    print(f'Your are question: {search}')
    answer = random.choice(list_one)
    print(f'Your are answer: {answer}')
if __name__=='__main__':
    main()