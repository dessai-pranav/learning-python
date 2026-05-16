

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def find_highest_bid(bid_dict):
    highest_bid = 0
    winner=""
    max(bid_dict)
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bid}.")
bids={}
continue_bidding = True
while continue_bidding:
    name = input("whats your name?:")
    price = int(input("whats your bid?: $"))
    bids[name] = price
    should_continue = input("would you like to continue? (y/n): \n").lower()
    if should_continue == "n":
        continue_bidding = False
        find_highest_bid(bids)
    elif should_continue == "y":
        print("\n"*20)








