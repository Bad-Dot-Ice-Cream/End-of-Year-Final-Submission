import os
import random

art = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         _'-------'_
                      ./-------------\.
                      /_______________\
        '''
print(art)

auctioned_piece = ["Old computer.", "A Cyruss egg.", "Singular hair from William J. Kissinger's sideburns.", "Pot of Greed from YugiOh.",
                    "Little moan from Noah Corll.", "Maid outfit tucked away in Cyruss's bedroom.", "Singular strand of beard hair from Mr. Sekol, teeming with wisdom.", "William's legendary Singlet."]

piece_desc = ["From the mythical jungles of Loopa Land...", "From the depths of a messy bedroom...", "From the inside of Yo Mama (i should know)...", "From the lost islands of the deadly Bermuda Triangle...", 
              "From the core of a dying star...", "From the dark side of the moon...", "From the forbidden depths of a middle school lost-and-found bin...", "From the Victorian era, smelling faintly of chimney soot and dramatic sighs...", "From the exact moment you realized you left the stove turned on..."]
chosen_piece = random.choice(auctioned_piece)

print(f"Today's auction piece,\n{random.choice(piece_desc)}")
print((chosen_piece))
print("\n")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\nThe winner is {winner} with a bid of ${highest_bid}, congrats and we hope you enjoy your new {chosen_piece}.\n")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?\n>  ")
    price = int(input("What is your bid?\n>  $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n>  ").lower()
    
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()