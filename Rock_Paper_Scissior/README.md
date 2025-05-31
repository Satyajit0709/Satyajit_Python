# Interactive Rock Paper Scissors Game with ASCII Art Visualization

This Python-based Rock Paper Scissors game provides an engaging command-line gaming experience with ASCII art visualizations and score tracking. Players compete against a computer opponent in this classic game while enjoying visual representations of each move and detailed score tracking.

The game implements the traditional Rock Paper Scissors rules with an intuitive numeric input system and clear visual feedback. It features persistent score tracking, round counting, and ASCII art representations of each move, making the gaming experience both visually appealing and interactive. The latest version (V4) includes enhanced features like round tracking and detailed game statistics upon exit.

## Repository Structure
```
.
├── Rock_Paper_Scissior_V1.py  # Initial version with basic game mechanics and ASCII art
├── Rock_Paper_Scissior_V2.py  # Added round tracking and enhanced score display
├── Rock_Paper_Scissior_V3.py  # Improved game flow and user feedback
└── Rock_Paper_Scissior_V4.py  # Final version with complete features and polished UI
```

## Usage Instructions
### Prerequisites
- Python 3.x installed on your system
- Terminal or command prompt access

### Installation
1. Clone the repository or download the Python files:
```bash
git clone [repository-url]
```

2. Navigate to the game directory:
```bash
cd [game-directory]
```

### Quick Start
1. Run the latest version of the game:
```bash
python Rock_Paper_Scissior_V4.py
```

2. Follow the on-screen prompts:
- Enter 0 for Rock
- Enter 1 for Paper
- Enter 2 for Scissors
- Enter 4 to Exit

### More Detailed Examples
```python
# Example game interaction:
Enter 0 for Rock, 1 for Paper and 2 for scissor or 4 to Exit
0
you have entered - Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer have entered - Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) 

YOU HAVE LOST  -- BETTER LUCK NEXT TIME ....
Round 1 | Score: You 0 - Computer 1
```

### Troubleshooting
Common issues and solutions:

1. Invalid Input Error
- Problem: "you have entered the Incorrect Value"
- Solution: Only enter numbers 0, 1, 2, or 4

2. Game Not Starting
- Verify Python installation: `python --version`
- Ensure you're in the correct directory
- Check file permissions: `chmod +x Rock_Paper_Scissior_V4.py`

## Data Flow
The game operates on a simple input-process-output loop where user input is collected, compared against computer selection, and results are displayed with ASCII art.

```ascii
[User Input] -> [Input Validation] -> [Computer Selection]
      |                                      |
      v                                      v
[Score Tracking] <- [Winner Determination] <- [Display Moves]
      |
      v
[Display Results]
```

Key component interactions:
1. User provides numeric input (0-2, 4)
2. Input is validated against acceptable range
3. Computer randomly generates its move
4. Both moves are displayed with ASCII art
5. Winner is determined based on game rules
6. Scores are updated and displayed
7. Process repeats until user exits
8. Final statistics are shown upon exit