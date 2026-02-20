import random
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
choice = input("choose a difficulty. type 'easy' or 'hard': ").lower()
def compare(attempt,comp_number):
    while attempt > 0 :
        print(f"You have {attempt} attempts left ")
        user_guess = int(input("Guess a number: "))
        if user_guess == comp_number:
            print(f"You got it! The answer was {comp_number}.")
            break
        elif user_guess > comp_number:
            print("too high.")
            print("guess again")
            attempt -= 1

        else:
            print("too low.")
            print("guess again")
            attempt -= 1
    if attempt == 0:
        print(f"you lose the number was {comp_number}")

def guess(difficulty):
    attempt = 10
    comp_number = random.randint(1, 100)

    if difficulty == "easy":
        compare(attempt,comp_number)
    elif difficulty == "hard":
        attempt = 5
        compare(attempt,comp_number)
    else:
        print("add something valid")

guess(choice)










