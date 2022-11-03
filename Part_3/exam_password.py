def main():
    password = input('Enter password: ')
    examination_password(password)


def examination_password(cod):
    correct = lower = upper_one = int_one = False
    if len(cod) >= 7:
        correct = True
    if cod.islower() is not True:
        lower = True
    if cod.isupper() is not True:
        upper_one = True
    if cod.isalnum():
        int_one = True
    if correct == True and lower == True and upper_one == True and int_one == True:
        print('Password Good')
    else:
        print('Password very Bad')


if __name__ == '__main__':
    main()
