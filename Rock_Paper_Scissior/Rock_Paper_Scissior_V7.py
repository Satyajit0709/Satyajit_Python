import random
import os
import time
import winsound  # For sound effects on Windows
import colorama  # For colored text
from colorama import Fore, Back, Style

# Initialize colorama
colorama.init(autoreset=True)

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

# Color themes
themes = {
    "default": {
        "header": Fore.WHITE + Style.BRIGHT,
        "text": Fore.WHITE,
        "win": Fore.GREEN + Style.BRIGHT,
        "lose": Fore.RED + Style.BRIGHT,
        "draw": Fore.YELLOW + Style.BRIGHT,
        "highlight": Fore.CYAN + Style.BRIGHT,
        "background": ""
    },
    "neon": {
        "header": Fore.MAGENTA + Style.BRIGHT,
        "text": Fore.CYAN,
        "win": Fore.GREEN + Style.BRIGHT,
        "lose": Fore.RED + Style.BRIGHT,
        "draw": Fore.YELLOW + Style.BRIGHT,
        "highlight": Fore.BLUE + Style.BRIGHT,
        "background": ""
    },
    "retro": {
        "header": Fore.YELLOW + Style.BRIGHT,
        "text": Fore.GREEN,
        "win": Fore.CYAN + Style.BRIGHT,
        "lose": Fore.RED + Style.BRIGHT,
        "draw": Fore.WHITE + Style.BRIGHT,
        "highlight": Fore.YELLOW + Style.BRIGHT,
        "background": ""
    }
}

# Game settings
settings = {
    "username": "Player",
    "theme": "default",
    "sound_effects": True
}

# Game variables
player_score = 0
computer_score = 0
rounds_played = 0
game_on = True
current_theme = themes["default"]

# Sound effects frequencies
sounds = {
    "win": 1000,
    "lose": 500,
    "draw": 750,
    "countdown": 600,
    "select": 800
}

# UI functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound(sound_type, duration=200):
    if settings["sound_effects"] and os.name == 'nt':  # Only on Windows
        try:
            winsound.Beep(sounds[sound_type], duration)
        except:
            pass  # Silently fail if sound doesn't work

def print_header():
    clear_screen()
    print(current_theme["header"] + "=" * 50)
    print(current_theme["header"] + f"ROCK PAPER SCISSORS GAME - {settings['username']}".center(50))
    print(current_theme["header"] + "=" * 50)
    print(current_theme["text"] + f"Score: {settings['username']} {player_score} - Computer {computer_score} | Rounds: {rounds_played}")
    print(current_theme["text"] + "-" * 50)

def countdown_animation():
    if not settings["sound_effects"]:
        return
        
    clear_screen()
    print(current_theme["highlight"] + "\n\nGet ready...")
    time.sleep(0.5)
    
    for word in ["Rock", "Paper", "Scissors"]:
        clear_screen()
        print(current_theme["highlight"] + f"\n\n{word}!".center(50))
        play_sound("countdown")
        time.sleep(0.7)
    
    clear_screen()
    print(current_theme["highlight"] + "\n\nSHOOT!".center(50))
    play_sound("select", 300)
    time.sleep(0.5)

def print_choices(user_choice, comp_choice):
    print(current_theme["text"] + "\nYour choice:")
    print(current_theme["highlight"] + f"{input_list[user_choice]}")
    print(current_theme["text"] + f"{images_list[user_choice]}")
    
    print(current_theme["text"] + "\nComputer is choosing", end="")
    for _ in range(3):  # Dramatic pause
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
    
    print(current_theme["text"] + "Computer's choice:")
    print(current_theme["highlight"] + f"{input_list[comp_choice]}")
    print(current_theme["text"] + f"{images_list[comp_choice]}")

def print_result(result, result_type="text"):
    color = current_theme["text"]
    if result_type == "win":
        color = current_theme["win"]
        play_sound("win")
    elif result_type == "lose":
        color = current_theme["lose"]
        play_sound("lose")
    elif result_type == "draw":
        color = current_theme["draw"]
        play_sound("draw")
        
    print("\n" + color + "=" * 50)
    print(color + result.center(50))
    print(color + "=" * 50)

def setup_game():
    global current_theme
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.CYAN + Style.BRIGHT + "ROCK PAPER SCISSORS - GAME SETUP".center(50))
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    
    # Username
    while True:
        username = input(Fore.WHITE + "\nEnter your username (or press Enter for 'Player'): ")
        if username.strip() or username == "":  # Allow empty for default
            if username.strip():
                settings["username"] = username
            break
        else:
            print(Fore.RED + "Please enter a username or press Enter for default!")
    
    # Theme selection
    while True:
        print(Fore.WHITE + "\nSelect a theme:")
        for i, theme in enumerate(themes.keys()):
            print(f"  {i+1} - {theme.capitalize()}")
        
        theme_choice = input("\nEnter theme number (or press Enter for default): ")
        if theme_choice == "":  # Allow empty for default
            break
        elif theme_choice.strip() and theme_choice.isdigit():
            theme_idx = int(theme_choice) - 1
            if 0 <= theme_idx < len(themes):
                theme_name = list(themes.keys())[theme_idx]
                settings["theme"] = theme_name
                break
            else:
                print(Fore.RED + f"Please enter a number between 1 and {len(themes)}!")
        else:
            print(Fore.RED + "Please enter a valid number or press Enter for default!")
    
    current_theme = themes[settings["theme"]]
    
    # Sound effects
    while True:
        sound_choice = input(Fore.WHITE + "\nEnable sound effects? (y/n, default: y): ").lower()
        if sound_choice in ["y", "n", ""]:  # Allow y, n, or empty for default
            if sound_choice == 'n':
                settings["sound_effects"] = False
            break
        else:
            print(Fore.RED + "Please enter 'y', 'n', or press Enter for default!")
    
    print(Fore.GREEN + "\nSettings saved! Game starting...")
    time.sleep(1.5)

# Main game
setup_game()

# Main game loop
while game_on:
    print_header()
    print(current_theme["text"] + "Options:")
    print(current_theme["text"] + "  0 - Rock")
    print(current_theme["text"] + "  1 - Paper")
    print(current_theme["text"] + "  2 - Scissors")
    print(current_theme["text"] + "  8 - Settings")
    print(current_theme["text"] + "  9 - Exit Game")
    
    try:
        user_input = int(input(current_theme["text"] + "\nEnter your choice: "))
        
        if user_input == 9:
            print_header()
            print_result("GAME OVER")
            print(current_theme["text"] + f"\nFinal Score: {settings['username']} {player_score} - Computer {computer_score}")
            
            if player_score > computer_score:
                print(current_theme["win"] + f"\n🏆 Congratulations! {settings['username']} won the game! 🏆")
            elif player_score < computer_score:
                print(current_theme["lose"] + "\n😢 Better luck next time! Computer won the game. 😢")
            else:
                print(current_theme["draw"] + "\n🤝 It's a tie game! 🤝")
                
            print(current_theme["text"] + "\nThanks for playing! Goodbye!")
            game_on = False
            
        elif user_input == 8:
            setup_game()
            
        elif user_input in range(0, 3):
            countdown_animation()
            computer_input = random.randint(0, 2)
            rounds_played += 1
            
            print_header()
            print_choices(user_input, computer_input)
            
            # Determine winner
            if (user_input == 0 and computer_input == 2) or (user_input == 2 and computer_input == 1) or (user_input == 1 and computer_input == 0):
                player_score += 1
                print_result(f"{settings['username']} WINS! 🎉", "win")
            elif (computer_input == 0 and user_input == 2) or (computer_input == 2 and user_input == 1) or (computer_input == 1 and user_input == 0):
                computer_score += 1
                print_result(f"{settings['username']} LOSES! 😞", "lose")
            else:
                print_result("IT'S A DRAW! 🤝", "draw")
                
            time.sleep(2)  # Pause to see the result
            
        else:
            print(current_theme["lose"] + "\nInvalid input! Please enter 0, 1, 2, 8, or 9 to exit.")
            time.sleep(2)
            
    except ValueError:
        print(current_theme["lose"] + "\nPlease enter a number!")
        time.sleep(2)

# Clean up colorama
colorama.deinit()