# game
Rock, Paper, Scissors game

1. Importing Required Modules
The game begins by importing the 'random' module, which is essential for generating random choices for the computer. This ensures that the game remains fair and unpredictable.
2. Defining Interactive Functions
To make the game interactive and enjoyable, several functions have been defined:
a. get_player_name(): This function prompts the player for their name, capturing their identity for a personalized gaming experience.
b. get_player_choice(): This function guides the player to choose between rock, paper, and scissors. A loop ensures that the player provides a valid choice. This step is crucial for the fairness of the game.
c. determine_winner(player_choice, computer_choice): The game's core logic resides here. This function evaluates the player's choice against the computer's choice based on the classic rock-paper-scissors rules. It determines whether the player wins, the computer wins, or if it's a tie.
d. play_game(): This function orchestrates the gameplay. It interacts with the user by displaying their choices and the computer's choices. It then calculates the result using the determine_winner() function, updates the score, and provides feedback to the player. The game continues until the player decides not to play again. Importantly, the 'play_game()' function ensures the game starts when the script is executed directly.
