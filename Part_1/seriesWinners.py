def main():
    file_series = open('WorldSeriesWinners.txt', 'r')
    list_team = []
    list_year = []
    for i in file_series:
        i = i.rstrip('\n')
        list_team.append(i)
    search = input('Enter name team: ').title()
    year_amount = 0
    for bum in range(len(list_team)):
        if list_team[bum] == search:
            year_amount += 1
            year_one = 1903 + bum
            if year_one == 1904 and year_one == 1994:
                year_one += 1
            list_year.append(year_one)

    print(f'Amount winners team {search} = {year_amount} and this years {list_year}')


if __name__ == '__main__':
    main()
