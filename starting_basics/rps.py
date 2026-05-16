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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice ==  0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
r = random.randint(0,2)
comp=[rock,paper,scissors]
print(comp[r])

if choice == r:
    print("its a draw")
elif choice == 0:
    if r == 2:
        print("you win")
    elif r == 1:
        print("you lose")
elif choice == 1:
    if r == 0:
        print("you win")
    elif r == 2:
        print("you lose")
elif choice == 2:
    if r == 0:
        print("you lose")
    elif r == 1:
        print("you win")

