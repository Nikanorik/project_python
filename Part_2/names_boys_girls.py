def main():
    file_boys = open('BoyNames.txt', 'r')
    file_girls = open('GirlNames.txt', 'r')
    boys = []
    girls = []
    for i in file_boys:
        i = i.rstrip('\n')
        boys.append(i)
    for num in file_girls:
        num = num.rstrip('\n')
        girls.append(num)
    choice = input("Enter your choice 'b'(boys), 'g'(girl), c(boy and girl): ")
    if choice == 'b':
        name_b = input('Enter name boy: ')
        if name_b in boys:
            print('This is one of the most popular names!')
        else:
            print('Name rare!')
    elif choice == 'g':
        name_g = input('Enter name girl: ')
        if name_g in girls:
            print('This is one of the most popular names!')
        else:
            print('Name rare!')
    elif choice == 'c':
        name_b_c = input('Enter name boy: ')
        name_g_c = input('Enter name girl: ')
        if name_b_c in boys and name_g_c in girls:
            print('This is popular names!')
        elif name_b_c not in boys and name_g_c in girls:
            print('Popular name only girl')
        elif name_b_c in boys and name_g_c not in girls:
            print('Popular name only boy')
        else:
            print('Names rare!!!')


if __name__ == '__main__':
    main()
