def main():
    file_us = open('USPopulation.txt', 'r')
    list_population = []
    list_different = []
    for i in file_us:
        i = int(i.rstrip('\n'))
        list_population.append(i)
        vari = list_population[0]
    for num in list_population:
        vari = num - vari
        list_different.append(vari)
        vari = num
    print(list_population)
    print(list_different)
    maximum = max(list_different)
    maxi_in = list_different.index(maximum)
    maxi_in_year = 1950 + maxi_in
    minimum = min(list_different[1:])
    mini_in = list_different.index(minimum)
    mini_in_year = 1950 + mini_in
    print(f'Year with most amount difference population {maxi_in_year} and difference = {maximum}')
    print(f'Year with least amount difference population {mini_in_year} and difference = {minimum}')


if __name__ == '__main__':
    main()
