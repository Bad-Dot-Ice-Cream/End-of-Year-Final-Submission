import random
import os

stages = [r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___''',

  r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
    _|___''',

  r'''
      _______
     |/      |
     |      (_)
     |      \|/
     |
     | 
     |
    _|___''',

  r'''
      _______
     |/      |
     |      (_)
     |      \|
     |
     |
     |
    _|___''',

  r'''
      _______
     |/      |
     |      (_)
     |       |
     |
     |
     |
    _|___''',

  r'''
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
    _|___''',

  r'''
      _______
     |/      |
     |
     |
     |
     |
    _|___''']

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Game chooses letter
word_list = ["monkey", "raptor", "cyruss", "william", "rat", "chimp", "blimp", "lips",
              "matter", "space", "banana", "falcon", "mantis", "beluga", "peace", "discord",
                "harmony", "chaos", "flag", "shrine", "spire", "crack", "foolish", "idiot",
                  "genius", "tablet", "kind", "radical", "class", "pray", "loathe", "glove",
                    "sword", "shield", "teach", "grass", "lamb", "shephard", "flick", "drama", "consume",
                      "freaky", "pause", "resume", "snippit", "folder", "bottle", "hashtag", "percent",
                        "lorax", "window", "trapped", "apple", "correct", "incorrect", "speak", "parrot",
                          "balloon", "train", "plane", "paper", "scissors", "science", "camel", "rodent",
                            "eclipse", "lunar", "unique", "smart", "jingle", "aardvark", "bishop", "faith",
                              "unholy", "lover", "onion", "melon", "grapefuit", "firework", "orange", "pidgeon",
                                "shark", "ocean", "rhubarb", "dream", "rapture", "murder", "capture", "gender",
                                  "natural", "filthy", "peasant", "patriarch", "royalty", "snake", "impact", "serpent",
                                    "avatar", "earth", "stormy", "thunder", "spirit", "wilderness", "island", "delta",
                                      "omega", "river", "lilac", "markiplier", "minecraft", "cocaine", "oregano", "jacket",
                                        "winter", "rigid", "frozen", "wretched", "splinter", "tortoise", "heart", "organ",
                                          "shallow", "landmass", "dolphin", "sassafras", "pocket", "button", "chair", "freelance",
                                            "starstruck", "hangman", "america", "china", "russia", "india", "africa", "walker",
                                              "alligator", "nevada", "trickshot", "flesh", "uncle", "grandpa", "grandma", "cousin",
                                                "wheat", "dynamite", "poetry", "write", "writhe", "drought", "famine", "conquest",
                                                  "disease", "cylinder", "company", "trail", "trace", "spider", "fright", "emerge",
                                                    "slobber", "shelf", "villain", "condition"]
chosenWord = random.choice(word_list)

userLives = 6

# Terminal wiping functionality
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Placeholder underscores
placeholder = ""
wordLength = len(chosenWord)
for position in range(wordLength):
    placeholder += "_ "
print(placeholder)

# Game over functionality and keeping track of guesses
gameOver = False
correct_letters = []
incorrect_letters = []
wrongLetters = ""

while not gameOver:
  print(f"=========== {userLives}/6 LIVES REMAINING ===========")
  userGuess = input("\nGuess a letter: ").lower()
  clear()

  # Preventing repeat & improper guesses
  if userGuess in correct_letters or userGuess in incorrect_letters:
     print("\n* You've already guessed this letter. *")
     continue
  
  guessLength = len(userGuess)
  if guessLength != 1 or userGuess.isalpha() == False:
     print("\n* You may only guess letters for this game. *")

  # Display (replaces placeholders with revealed letters)
  display = ""


# Check if right/wrong (if user guessed letter is in word)
  if userGuess in chosenWord:
    correct_letters.append(userGuess)

  for letter in chosenWord:
      if letter == userGuess:
          display += letter
      elif letter in correct_letters:
         display += letter
      else:
          display += " _ "
  

  if userGuess not in chosenWord and userGuess not in incorrect_letters:
    incorrect_letters.append(userGuess)

  wrongLetters = " ".join(incorrect_letters)

      
  print(display)

  if userGuess not in chosenWord:
      userLives -= 1
      print(f"\n{userGuess} is not in the word. You lose a life.")

  if wrongLetters != "":
    print(f"\nThe word does not have: {wrongLetters}\nWhich you have already guessed.\n")

  if userLives == 0:
      gameOver = True
      print(f"Your word was {chosenWord}\n*** You lose. ***")
      break

  if "_" not in display:
      print("*** You win! ***")
      break

  print(stages[userLives])