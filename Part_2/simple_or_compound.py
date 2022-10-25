def main():
    number = int(input('Enter number from 1 to 100: '))
    list_one = []
    list_two = []
    for i in range(2,number+1):
        for num in range(1,i):
            if num > 1 and i % num == 0:
                list_one.append(i)
                break
            elif num > 1 and i % num != 0:
                list_two.append(i)
                break
    print(f'Number simple = {list_two} and compound = {list_one}')
if __name__ == '__main__':
    main()

