import random


def main():
   list_number = []
   for i in range(7):
       articl = ''
       for i in range(7):
           num=random.randint(0,9)
           articl+=str(num)
       list_number.append(articl)
   print(list_number)

if __name__ == '__main__':
    main()