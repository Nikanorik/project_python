def main():
    file_country = open('charge_accounts.txt', 'r')
    list_number = []
    for i in file_country:
        i = i.rstrip('\n')
        list_number.append(int(i))
    print(list_number)
    search = int(input('Enter number: '))
    if search in list_number:
        number_l = list_number.index(search)
        print(f'Number yes in position {number_l + 1}')
    else:
        print('Number NO!')
    file_country.close()


if __name__ == '__main__':
    main()
