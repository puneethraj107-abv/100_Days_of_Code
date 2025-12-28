# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)
print("welcome to blind auction program")

# def find_highest_bidder(highest_bidder):
#    highest_bid=0
#    winner=""
#    for bidder in highest_bidder:
#        bid_amount=highest_bidder[bidder]
#        if bid_amount>highest_bid:
#            highest_bid=bid_amount
#            winner=bidder
#    print(f" the winner in {winner} with a bid of ${highest_bid}")

bids={}
continue_bidding=True
while continue_bidding:
    name = input("what is your name?  ")
    price = int(input("what is your bid?  "))
    bids[name]=price
    continuation=input("any other bids. type yes or no").lower()
    if continuation=="no":
        continue_bidding=False
        max_key, max_value = max(bids.items(), key=lambda x: x[1])
        print(f"highest bidder is{max_key}, with an amount of {max_value}")

    elif continuation =="yes":
        print("\n"*20)



