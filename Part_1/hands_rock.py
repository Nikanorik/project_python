import random

print('Game Rock - Paper - Scissors')
Rock = 0
rock1 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = 1
paper1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors = 2
scissors1 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
comp_step = random.randint(0,2)
user_step = input('Enter Paper(P), Rock(R), Scissors(S): ').lower()
if comp_step == 0:
    print(f'Comp:\n{rock1}')
elif comp_step == 1:
    print(f'Comp:\n{paper1}')
elif comp_step == 2:
    print(f'Comp:\n{scissors1}')
if user_step == 'p' or user_step == 'paper':
    user_step=1
    print(f'User:\n{paper1}')
elif user_step == 'r' or user_step == 'rock':
    user_step= 0
    print(f'User:\n{rock1}')
elif user_step =='s' or user_step =='scissors':
    user_step = 2
    print(f'User:\n{scissors1}')
else:
    print('Error input! ')
    user_step = 'Error'
if user_step!= 'Error':
    if (comp_step == 0 and user_step == 2) or (comp_step ==1 and user_step == 0) or (comp_step ==2 and user_step == 1):
        print('Winner Comp!')
    elif comp_step == user_step:
        print('Draw')
    else:
        print('Winner User!!!')





