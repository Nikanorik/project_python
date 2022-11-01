def main():
    file_new = open('tokens.csv','r')
    read_text = file_new.readlines()
    for i in read_text:
        i=i.rstrip('\n')
        numer = i.split(',')
        summa=0
        for num in numer:
            summa+=int(num)
        print(f'Middle grade student: {summa/len(numer)}')
    file_new.close()

if __name__ == '__main__':
    main()