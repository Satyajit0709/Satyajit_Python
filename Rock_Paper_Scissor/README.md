# Interactive Rock Paper Scissors Game with Enhanced Visual and Audio Features

A modern, feature-rich implementation of the classic Rock Paper Scissors game built in Python. This game offers an engaging player experience with ASCII art visuals, customizable color themes, sound effects, and an intuitive user interface.

The game enhances the traditional Rock Paper Scissors experience with multiple features:
- Customizable player usernames and game settings
- Three distinct color themes (Default, Neon, and Retro)
- ASCII art representations of game elements
- Sound effects for game actions (Windows only)
- Real-time score tracking and round counting
- Interactive countdown animations
- Comprehensive game statistics and end-game summary

## Repository Structure
```
Rock_Paper_Scissior/
├── Archive_doc/               # Documentation archive
│   └── README.md             # Archive documentation
├── requirements.txt          # Project dependencies (colorama)
├── Rock_Paper_Scissior_Enhanced.py   # Main enhanced version with all features
├── Rock_Paper_Scissior_UI.py         # UI-focused version
└── Rock_Paper_Scissior_V[1-7].py     # Development versions showing progression
```

## Usage Instructions
### Prerequisites
- Python 3.6 or higher
- Required packages:
  ```
  colorama==0.4.4
  ```
- Windows OS for sound effects (optional)

### Installation
1. Download the code:
download code from [https://github.com/Satyajit0709/Satyajit_Python ](https://github.com/Satyajit0709/Satyajit_Python/tree/master/Rock_Paper_Scissor)

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Version details 

- V1 - Base Version 
- V2 - Loop added to continue game until exit code is added
- V3 - Add score of computer and Player
- V4 - Added a final score of computer and Player at the end of the Game
- V5 - Improvised UI and final score Updates 
- V6 -
  1.   Allow players to choose their username
  2.   Let players customize the game colors or themes
  3. Option to toggle sound effects on/off
  4. 	Add a "Rock, Paper, Scissors, Shoot!" countdown animation
  5.  Dramatic reveal of computer's choice with a short delay
- V7 -
  1. Add a counter which will also show how many numbers of round has been completed.
  2. Add a Logic to maintain a score of the player and reset the score after execution ends.

### Quick Start
1. Run the enhanced version:
```bash
python Rock_Paper_Scissior_Enhanced.py
```

2. Follow the setup prompts to:
   - Enter your username (or press Enter for default)
   - Select a color theme
   - Enable/disable sound effects

3. Play the game using these commands:
   - `0` - Choose Rock
   - `1` - Choose Paper
   - `2` - Choose Scissors
   - `8` - Access Settings
   - `9` - Exit Game

### More Detailed Examples
```python
# Example game flow
1. Enter username: "Player1"
2. Select theme: "2" (for Neon theme)
3. Enable sound effects: "y"
4. Choose Rock: "0"
   > Computer randomly selects
   > Winner is determined
   > Scores are updated
5. Access settings: "8"
   > Modify username, theme, or sound settings
6. Exit game: "9"
   > Final scores and winner displayed
```

### Troubleshooting
Common Issues:
1. Sound effects not working
   - Verify you're on Windows OS
   - Check system sound settings
   - Try running with administrator privileges

2. Display issues
   - Ensure terminal supports ASCII characters
   - Try different color themes
   - Update colorama package

3. Input errors
   - Enter only numbers 0-2, 8, or 9
   - Avoid empty inputs
   - Don't use special characters

## Data Flow
The game follows a simple input-process-output cycle with enhanced visual and audio feedback.

```ascii
[User Input] -> [Input Validation] -> [Game Logic] -> [Result Calculation]
      ^                                                      |
      |                                                      v
[Display Results] <- [Visual/Audio Effects] <- [Score Update]
```

Component Interactions:
1. User provides input through number keys (0-2, 8, 9)
2. Input is validated and processed
3. Computer generates random choice
4. Game logic determines winner based on classic rules
5. Scores are updated and stored in memory
6. Visual feedback is displayed with ASCII art
7. Sound effects play based on game events (Windows only)
8. Results are shown with colored text and animations
