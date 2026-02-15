import random

word_list = ["aardvark", "baboon", "camel"]
chosen_Word = random.choice(word_list)
print(chosen_Word)
guess = input("Enter a letter: ").lower()
for l in chosen_Word:
    if guess == l:
        print("right")
    else:
        print("wrong")