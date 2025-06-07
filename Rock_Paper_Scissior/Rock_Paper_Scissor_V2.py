import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images_list = [rock,paper,scissors]
input_list = ["Rock" , "Paper" , "Scissor"]

# Initialize player and computer scores and round counter
player_score = 0
computer_score = 0
rounds_played = 0
game_on = True

while game_on:
    user_input = int(input("Enter 0 for Rock , 1 for Paper and 2 for scissor or 4 to Exit \n"))
    computer_input=0
    if user_input == 4:
        print(f"Game Over! Total Rounds Played: {rounds_played}")
        print(f"Final Score: You {player_score} - Computer {computer_score}")
        if player_score > computer_score:
            print("Congratulations! You won the game!")
        elif player_score < computer_score:
            print("Better luck next time! Computer won the game.")
        else:
            print("It's a tie game!")
        print("Thanks for playing! Goodbye!")
        game_on = False
    elif user_input in range (0,3):
        print(f" you have entered - {input_list[user_input]}   {images_list[user_input]}")
        computer_input = random.randint(0,2)
        print(f" Computer have entered - {input_list[computer_input]}   {images_list[computer_input]}")
        ## Increment round counter
        rounds_played += 1
        
        ## check the Posibbilities of user wins
        if (user_input == 0 and computer_input ==2 ) or (user_input == 2 and computer_input ==1) or (user_input == 1 and computer_input ==0):
            player_score += 1
            print("YOU HAVE WON  -- CHEERS")
            print(f"Round {rounds_played} | Score: You {player_score} - Computer {computer_score}")
        elif (computer_input == 0 and user_input ==2 ) or (computer_input == 2 and user_input ==1) or (computer_input == 1 and user_input ==0):
            computer_score += 1
            print("YOU HAVE LOST  -- BETTER LUCK NEXT TIME ....")
            print(f"Round {rounds_played} | Score: You {player_score} - Computer {computer_score}")
        elif computer_input == user_input:
            print("IT'S DRAW , PLAY AGAIN ....")
            print(f"Round {rounds_played} | Score: You {player_score} - Computer {computer_score}")
    else:
        print("you have entered the Incorrect Value. Please enter 0, 1, 2, or 4 to exit")