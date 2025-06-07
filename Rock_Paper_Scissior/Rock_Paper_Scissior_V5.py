import random
import os
import time

# ASCII art for game elements
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

# Game assets
images_list = [rock, paper, scissors]
input_list = ["Rock", "Paper", "Scissors"]

# Game variables
player_score = 0
computer_score = 0
rounds_played = 0
game_on = True

# UI functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print("=" * 50)
    print("ROCK PAPER SCISSORS GAME".center(50))
    print("=" * 50)
    print(f"Score: You {player_score} - Computer {computer_score} | Rounds: {rounds_played}")
    print("-" * 50)

def print_choices(user_choice, comp_choice):
    print("\nYour choice:")
    print(f"{input_list[user_choice]}")
    print(f"{images_list[user_choice]}")
    
    print("\nComputer's choice:")
    print(f"{input_list[comp_choice]}")
    print(f"{images_list[comp_choice]}")

def print_result(result):
    print("\n" + "=" * 50)
    print(result.center(50))
    print("=" * 50)

# Main game loop
while game_on:
    print_header()
    print("Options:")
    print("  0 - Rock")
    print("  1 - Paper")
    print("  2 - Scissors")
    print("  9 - Exit Game")
    
    try:
        user_input = int(input("\nEnter your choice: "))
        
        if user_input == 9:
            print_header()
            print_result("GAME OVER")
            print(f"\nFinal Score: You {player_score} - Computer {computer_score}")
            
            if player_score > computer_score:
                print("\n🏆 Congratulations! You won the game! 🏆")
            elif player_score < computer_score:
                print("\n😢 Better luck next time! Computer won the game. 😢")
            else:
                print("\n🤝 It's a tie game! 🤝")
                
            print("\nThanks for playing! Goodbye!")
            game_on = False
            
        elif user_input in range(0, 3):
            computer_input = random.randint(0, 2)
            rounds_played += 1
            
            print_choices(user_input, computer_input)
            
            # Determine winner
            if (user_input == 0 and computer_input == 2) or (user_input == 2 and computer_input == 1) or (user_input == 1 and computer_input == 0):
                player_score += 1
                print_result("YOU WIN! 🎉")
            elif (computer_input == 0 and user_input == 2) or (computer_input == 2 and user_input == 1) or (computer_input == 1 and user_input == 0):
                computer_score += 1
                print_result("YOU LOSE! 😞")
            else:
                print_result("IT'S A DRAW! 🤝")
                
            time.sleep(2)  # Pause to see the result
            
        else:
            print("\nInvalid input! Please enter 0, 1, 2, or 9 to exit.")
            time.sleep(2)
            
    except ValueError:
        print("\nPlease enter a number!")
        time.sleep(2)