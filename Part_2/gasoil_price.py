import matplotlib.pyplot as pit
def main():
    file_new = open('1994_Weekly_Gas_Averages.txt', 'r')
    list_y = []
    list_x = []
    for i in file_new:
        i = i.rstrip('\n')
        list_y.append(i)
    for i in range(1,53):
        list_x.append(i)
    pit.plot(list_x,list_y)
    pit.xlim(xmin=1, xmax=52)
    pit.xticks(list_x,list_x)
    pit.title('Price oil weekly: ')
    pit.xlabel('number week')
    pit.ylabel('price oil')
    pit.grid(True)
    pit.show()
if __name__=='__main__':
    main()