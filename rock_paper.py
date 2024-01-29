import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock,paper,scissors]
index = random.randint(0, len(list)-1)
computer = list[index]

user = input("Rock, Paper or Scissors? ").lower()
if user == 'rock':
  print(rock)
  if computer == rock:
    print(rock)
    print('Draw!')
  elif computer == paper:
    print(paper)
    print('You lose')
  elif computer == scissors:
    print(scissors)
    print('You win!')

elif user == 'paper':
  print(paper)
  if computer == paper:
    print(paper)
    print('Draw!')
  elif computer == rock:
    print(rock)
    print('You win!')
  elif computer == scissors:
    print(scissors)
    print('You lose!')

elif user == 'scissors':
  print(scissors)
  if computer == rock:
    print(rock)
    print('You lose!')
  elif computer == paper:
    print(paper)
    print('You win!')
  elif computer == scissors:
    print(scissors)
    print('Draw!')
else:
  print('Incorrect Input.')


    
  



