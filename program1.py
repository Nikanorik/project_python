import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = int(input('Enter amount symbol to password: '))
nr_numbers = int(input('Enter amount numbers to password: '))
nr_symbols = int(input('Enter amount symbols to password: '))
letters_line = [letters, numbers, symbols]
choice_letters = random.choice(letters_line)
a = 0
b = 0
if choice_letters == numbers:
    a += 1
elif choice_letters == symbols:
    b += 1
elif choice_letters == letters:
    a = 0
    b = 0
element = random.choice(choice_letters)
for i in range(nr_letters - 1):
    all_number = random.choice(letters_line)
    if all_number == numbers:
        a += 1
    elif all_number == symbols:
        b += 1
    if a <= nr_numbers and b <= nr_symbols:
        for vebs in random.choice(all_number):
            element = element + vebs
    else:
        if a < nr_numbers:
            element = element + random.choice(random.choice([numbers, letters]))
            a += 1
        elif b < nr_symbols:
            element = element + random.choice(random.choice([symbols, letters]))
            b += 1
        else:
            element = element + random.choice(random.choice([letters]))

print(element)
