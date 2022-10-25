import matplotlib.pyplot as pit


def main():
    file_new = open('monthly_expenses.txt', 'r')
    list_new = []
    list_two = []
    list_one = []
    for i in file_new:
        i = i.rstrip('\n')
        list_new.append(i)
    for num in range(len(list_new)):
        if num % 2 != 0:
            list_two.append(list_new[num])
        else:
            list_one.append((list_new[num]))
    print(list_two)
    pit.title('Expenses from month!')
    pit.pie(list_two, labels=list_one)
    pit.show()


if __name__ == '__main__':
    main()
