import random
import os

# Terminal clearing functionality
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Hands and deck
print("~~~~~~~~~~~~~~~~~~~~~~~~")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
userHand = []
gameHand = []
gameChance = [1, 1, 1, 2]

# Game starting functionality
startGame = input("Would you like to play a game of Blackjack?\n>  ").lower()
user_game_over = False
dealer_game_over = False

# Players (user & game) receive 2 random card/s from deck on the first turn
def user_init_Turn():
    # Draws twice
    userDraw = random.choice(cards)
    userHand.append(userDraw)
    userDraw = random.choice(cards)
    userHand.append(userDraw)
    userScore = sum(userHand)
    print(f"Your hand: {userHand} = {userScore}")

def game_init_Turn():
    gameDraw = random.choice(cards)
    gameHand.append(gameDraw)
    gameDraw = random.choice(cards)
    gameHand.append(gameDraw)
    gameScore = sum(gameHand)
    print(f"Opponent hand: {gameHand} = {gameScore}")

# All other functions
def gameHit():
    global dealer_game_over
    gameDraw = random.choice(cards)
    gameScore = sum(gameHand)
    if gameDraw == 11:
        if (gameScore + 11) > 21:
            gameDraw = 1
    gameHand.append(gameDraw)
    gameScore = sum(gameHand)
    if gameScore > 21:
        dealer_game_over = True
    elif gameScore >= 15:
        gameChance[-2] = 2
        gameChance[-3] = 2
        print(gameChance)
    print(f"The opponent decides to Hit!\nOpponent hand: {gameHand} = {gameScore}")

def gameStand():
    gameScore = sum(gameHand)
    print(f"\nThe opponent decides to Stand!\n\nOpponent hand: {gameHand} = {gameScore}")

def userHit():
    global user_game_over
    userDraw = random.choice(cards)
    userScore = sum(userHand)
    if userDraw == 11:
        if (userScore + 11) > 21:
            userDraw = 1
    userHand.append(userDraw)
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    userScore = sum(userHand)
    if userScore > 21:
        user_game_over = True
    print(f"Your hand: {userHand} = {userScore}")

def userStand():
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    userScore = sum(userHand)
    print(f"Your hand: {userHand} = {userScore}")

user_init_Turn()
game_init_Turn()

def findChance():
    find_chance = random.choice(gameChance)
    if find_chance == 1:
        gameHit()
    else:
        gameStand()

# Game looping
while not user_game_over and not dealer_game_over:
    hit_or_stand = input("\nType 'y' to Hit, receiving a new card. Type 'n' to Stand, ending your turn without receiving a card.\n>  ").lower()
    if hit_or_stand == "y":
        clear()
        userHit()
        findChance()
    elif hit_or_stand == "n":
        clear()
        userStand()
        findChance()
        
# Game over
if dealer_game_over == True:
    print("\nYou WIN!")
elif user_game_over == True:
    print("\nBUST")
print("~~~~~~~~~~~~~~~~~~~~~~~~")