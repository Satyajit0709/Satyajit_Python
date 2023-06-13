import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["APPLE" , "BANANA" , "PAPAYA" , "MANGO" , "STRAWBERRY" , "GUAVA", "ORANGE"]

random_word = random.choice(word_list)
# print("Random word selected  is " + random_word )
Dash_list=[]
for position in range(len(random_word)):
    Dash_list += "_"
print("Dash List -  ")
print(Dash_list)
win_or_lose = True
counter=6
##for chances in range(7):
while win_or_lose:

    user_input = input("Guess the letters in the word - CLUE - it is one Fruit \n")
    if user_input in random_word:
        for letter_position in range(len(random_word)):
            if random_word[letter_position] == user_input:
                Dash_list[letter_position] = user_input
            else:
                pass
    else:
        print("Not matching , you loose one chance")
        print(stages[counter])
        counter -=1
    print(Dash_list)
    if "_" in Dash_list and counter == -1:
        print("All words are not replaced - YOU LOST")
        win_or_lose=False
    elif not "_" in Dash_list:
        print("All words are replaces - Congrats you won")
        win_or_lose = False
