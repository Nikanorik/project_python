def main():
    list_shu = []
    beta = 0
    gamma = 0
    sigma = 0

    for i in range(3):
        list_lo = []
        for num in range(3):
            number_new = int(input('Enter number: '))
            list_lo.append(number_new)
            if num == 0:
                beta += number_new
            elif num == 1:
                gamma += number_new
            elif num == 2:
                sigma += number_new

        list_shu.append(list_lo)
    diagonal1 = list_shu[0][0] + list_shu[1][1] + list_shu[2][2]
    diagonal2 = list_shu[0][2] + list_shu[1][1] + list_shu[2][0]
    for i in list_shu:
        print(i)
    if beta == gamma == sigma == diagonal1 == diagonal2 == sum(list_shu[0]) == sum(list_shu[1]) == sum(list_shu[2]):
        print('Square Lo Shu')
    else:
        print('Square usually!!!')


if __name__ == '__main__':
    main()
