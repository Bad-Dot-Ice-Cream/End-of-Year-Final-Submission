import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# User inputs time in seconds
running = True
while running == True:
    print("________________")
    init_time = float(input("Please input the time in seconds > "))

# Calculating to minutes, seconds
    minutes = int(init_time // 60)
    seconds = round(init_time % 60)
    print("\n")
    print(f"{minutes} minute(s) and {seconds} second(s)")
    print("\n")
    print("________________")
    try_again = input("\nWould you like to try again?\n>  ")
    if try_again == "no" or try_again == "n":
        running = False
    clear()

if running == False:
    print("________________\n")
    print("Thanks for stopping by!")
    print("\n________________")