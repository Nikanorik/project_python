import random

print('Game Hangman!')
word_list = ['phone','table','goose', 'important']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
book = random.choice(word_list)
print(book)
print(len(book))
print(book[2])
len_book = len(book)
list_word = []
for i in range(len_book):
    list_word+='_'
print(list_word)
print('Guess the letter!')
end_book = True
hangman=6
while end_book:
    mystery_attempt = input('Enter letter: ').lower()
    if mystery_attempt in book:
        for position in range(len_book):
            letter = book[position]
            if letter == mystery_attempt:
                list_word[position]=mystery_attempt
        print(list_word)
        if '_' not in list_word:
            end_book= False
            print('You Win!!!')
    else:
        hangman -=1
        print(stages[hangman])
        if hangman==0:
            print('You Lose!')
            break








