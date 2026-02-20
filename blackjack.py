logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Returns the score of the given list of cards."""

    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0

    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)

    return score


def compare(user_score, computer_score):
    """Compares scores and prints result."""

    if user_score == computer_score:
        print("🤝 It's a draw!")
    elif computer_score == 0:
        print("😞 You lose. Computer has Blackjack!")
    elif user_score == 0:
        print("🎉 You win with a Blackjack!")
    elif user_score > 21:
        print("💥 You went over. You lose!")
    elif computer_score > 21:
        print("🎉 Computer went over. You win!")
    elif user_score > computer_score:
        print("🎉 You win!")
    else:
        print("😞 You lose!")


while True:
    play_game = input("\nDo you want to play Blackjack? Type 'y' to play or 'n' to quit: ").lower()

    if play_game != "y":
        print("Thanks for playing! 👋")
        break

    print(logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards} | Current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Auto stop if blackjack or bust
        if user_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to draw another card or 'n' to stand: ").lower()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n=== Final Results ===")
    print(f"Your final hand: {user_cards} | Final score: {user_score}")
    print(f"Computer's final hand: {computer_cards} | Final score: {computer_score}")

    compare(user_score, computer_score)
