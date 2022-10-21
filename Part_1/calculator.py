from art import logo
def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2
print(logo)
def calculation():
    num1 = float(input('What is the first number?: '))

    operations = {
        '+': add, '-': substract, '*': multiply, '/': divide
    }
    flag = 'y'
    while flag == 'y':
        for symbol in operations:
            print(symbol)

        variant = input('Enter operation "+","-","*","/": ')
        num2 = float(input('What is the next number?: '))
        operator_calculation = operations[variant]
        answer = operator_calculation(num1, num2)
        print(f'{num1} {variant} {num2} = {answer:.2f} ')
        num1 = answer
        flag = input('You want to next calculation? Enter "y"(if yes) or "n"(if no) or "g"(if next new start): ')
        if flag == 'g':
            calculation()
        elif flag != 'y' and flag != 'g':
            print('Thank you for using the calculation!!!')

calculation()