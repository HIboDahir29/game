#import random module to generate random choices for the computer
import random

# Prompts the user for their name
def get_player_name():
    name = input('Enter your name for the game: ')
    return name

#Prompts the user to chooose between rock,paper and scissors
def get_player_choice():
    while True:
        choice = input('Choose Rock, Paper, Scissors: ')
        if choice in ['Rock', 'Paper', 'Scissors']:
            return choice
        else:
            print('Invalid choice. Please choose again')  

# determing the winner of the game
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print('It is a tie!')
    elif (
        (player_choice == 'Rock' and computer_choice == 'Scissors') or
        (player_choice == 'Paper' and computer_choice == 'Rock') or
        (player_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        return 'You Win!'
    else:
        return'Computer Wins!'
        
# playing the game and keeping track of the score of both the computer and the player
def play_game():
    player_name = get_player_name()
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

        print(f'{player_name} you chose {player_choice}')
        print(f'Computer chose {computer_choice}')

        result = determine_winner(player_choice,computer_choice)
        print(result)

        if result == 'You Win!':
            player_score += 1
        elif result == 'Computer Wins!':
            computer_score += 1
        print(f'Score for {player_name} is: {player_score}, Computer Score: {computer_score} ')

        play_again = input('Do you want to go another round? (yes or no): ')
        if play_again.lower() != 'yes':
            print(f'Thanks for playing {player_name}')
            break

play_game()         
              