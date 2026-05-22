import sys, time
import random

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    return ""

def slow_type(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.05)
    return ""

def fast_type(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    return ""

    # Boss fight section
    # Defining Boss
class Boss:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.dodging = False
        self.alive = True
        self.turn_cycle = 0

    def take_damage(self, amount):
        if self.dodging:
            if random.random() < 0.6:
                fast_type(f"\n{self.name} dodges the attack!")
                self.dodging = False
                return
            else:
                fast_type(f"\n{self.name} fails to dodge!")

        self.dodging = False    
        self.health -= amount
        fast_type(f"\n{self.name} is dealt {amount} damage!")

        if self.health <= 0:
            self.health = 0
            self.alive = False
            fast_type(f"\n{self.name} has been defeated!")

    def attack(self):
        fast_type(f"\n{self.name} unleashes it's fangs, dealing {self.damage} damage!")
        return self.damage

    def next_move(self):
        self.turn_cycle += 1

        if self.turn_cycle % 3 == 1:
            fast_type("\nThe COBRA thrashes about violently. rearing up to strike...")
            return "charge"

        elif self.turn_cycle % 3 == 2:
            fast_type("\nThe COBRA unleashes it's fangs in a vicious burst of speed!")
            return "attack"

        elif self.turn_cycle % 3 == 0:
            fast_type("\nThe COBRA moves swiftly, making itself harder to hit!")
            self.dodging = True
            return "dodge"

    def is_alive(self):
        return self.alive

    # Defining Player
class Player:
    def __init__(self, name, health, stamina, have_club):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.have_club = have_club
        self.alive = True
        self.guard = False

    def attack(self):
        if self.stamina < 10:
            fast_type("You're too exhausted to attack!'")

        if self.have_club:
            damage = random.randint(25, 35)
        else:
            damage = random.randint(10, 35)

        self.stamina -= 10
        fast_type(f"{self.name} attacks for {damage} damage!")
        return damage

    def guard_up(self):
        if self.stamina < 25:
            fast_type('You\'re too exhausted to guard!')
            return

        self.guard = True
        self.stamina -= 25
        fast_type(f"{self.name} brace for impact!")

    def rest(self):
        recovered = int(self.stamina * 0.40)
        self.stamina += recovered

        if self.stamina > 100:
            self.stamina = 100
        fast_type(f"{self.name} rests and recovers {recovered} stamina!")

    def take_damage(self, amount):
        if self.guard:
            amount = int(amount * 0.3)  # 70% reduction
            self.guard = False

        self.health -= amount
        fast_type(f"\n{self.name} take {amount} damage!")

        if self.health <= 0:
            self.health = 0
            self.alive = False
            fast_type(f"{self.name} has fallen!")

    def is_alive(self):
        return self.alive

    # More functionality
def start_boss_fight(haveClub):

    player = Player("You", 100, 100, haveClub)
    cobra = Boss("COBRA", 115, 32)

    fast_type('\n_________________________')
    fast_type("\nThe battle begins!\n")

    while player.is_alive() and cobra.is_alive():

        print(f"\nYou: {player.health} HP | {player.stamina} stamina")
        print(f"COBRA: {cobra.health} HP\n")

        action = input("\nattack / guard / rest:\n> ").lower()

        if action == "attack":
            dmg = player.attack()
            if dmg > 0:
                cobra.take_damage(dmg)

        elif action == "guard":
            player.guard_up()

        elif action == "rest":
            player.rest()

        else:
            fast_type("You hesitate, losing your oppurtunity to make a move.")

        # Cobra turn
        move = cobra.next_move()

        if move == "attack":
            dmg = cobra.attack()
            player.take_damage(dmg)

    # Outcome
    if player.is_alive():
        fast_type("\nYou have defeated the COBRA, well done!\nGame Over.")
    else:
        fast_type("\nYou were slain by the COBRA...\nGame Over.")


# Actual game & story
art = r'''                888                     
                888                     
                888                     
 .d8888b .d88b. 88888b. 888d888 8888b.  
d88P/   d88\/88b888 \88b888P/     \88b 
888     888  888888  888888    .d888888 
Y88b.   Y88..88P888 d88P888    888  888 
 \Y8888P \Y88P/ 88888P/ 888    \Y888888 '''
print(art)
print('\n')
print("---------------------")
print('Welcome to COBRA.')
print('Your mission is to KILL the COBRA.')
print('\n')


choice1 = input(
    'You awaken at a crossroad, where do you want to go?\nType "left" or "right".\n>  ').lower()


if choice1 == "left":

    choice2 = input(
        'As you walk you see in the distance a... table? Looking around, you sense no other prescence. ' \
        'On the table lies a single wodden club.\nType "acquire" to take it for yourself or "leave" to continue fowards.\n>  ').lower()
    if choice2 == "acquire":
        haveClub = True
    else:
        haveClub = False
    
    choice3 = input(
        'You\'ve arrived at a lake, there is an island in the center of the lake.\nType "wait" to wave a passing boat or "swim" to simply swim across.\n> ').lower()

    if choice3 == "wait":

        choice4 = input(
            'You successfully reach the island unharmed and thank the boatman as you depart. As you venture to the island, you approach a house with three doors.\n'
        'One yellow, from which hissing can be heard from within.\n'
        'One green, from which you hear no apparent sound.\n'
        'And one blue, from which you hearing the loud gush of running water. Which color door do you choose to enter?\n> ').lower()

        if choice4 == "green":
            typing('You open the door slowly, a soft crack is heard as you step inside the room. Suddenly you hear a hiss as a sharp pain pierces your side.' \
            '\nYour vision blurs and the lights fade as you fall upon the nest of the COBRA. The last thing you see is the vile creature slithering out into freedom... GAME OVER.')

        elif choice4 == "yellow":
            fast_type('You open the door cautiously, locking eyes with the COBRA, who hisses violently at your prescence.')
            start_boss_fight(haveClub)

        elif choice4 == "blue":
            fast_type('As you cautiously clutch the doornob for life, the sound of water grows even louder. Suddenly, the door flings open and you are cast into an underground river.' \
            '\nYou do not know where it leads, however, as your vision darkens and your lungs scream, you know you will likely not live to find out... GAME OVER.')

        else:
            slow_type('You chose a door that does not exist. The stress of the decision causes your vision to blur as you collapse, clutching your heart in agony. Such a diffcult choice isn\'t for everyone after all...')

    elif choice3 == "swim":
        typing('Suddenly a massive catfish leaps onto the shoreline and comes upon you, devouring you quickly without hesitation. It is very painful, albeit fast. GAME OVER.')

    else:
        typing('Suddenly a massive catfish leaps onto the shoreline and comes upon you, devouring you quickly without hesitation. It is very painful, albeit fast. GAME OVER.')


else:
    slow_type('You unexpectedly fall into a hole, from which you are unable to escape. GAME OVER.')