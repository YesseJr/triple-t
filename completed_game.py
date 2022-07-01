#!/usr/bin/python3

# Author: Waython Yesse
# Address: waythonny@yahoo.com
# Occupation: Software Engineering Student at ALX Africa & Holberton School of Technology
# Year: 2022

# Libraries
import os
import time
import random
import tkinter
from colorama import Fore # Python Library for colouring


# The Game's printing Functions
def print_game(board):

    print(Fore.LIGHTBLUE_EX +"\n")
    print(Fore.GREEN +"\t     |     |")
    print(Fore.GREEN +"\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print(Fore.YELLOW +'\t_____|_____|_____')
 
    print(Fore.YELLOW +"\t     |     |")
    print(Fore.CYAN +"\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print(Fore.CYAN +'\t_____|_____|_____')
 
    print(Fore.YELLOW +"\t     |     |")
 
    print(Fore.BLUE +"\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print(Fore.BLUE +"\t     |     |")
    print(Fore.LIGHTBLUE_EX +"\n")
    print(Fore.YELLOW +"\tGame By Waython Yesse")
    print(Fore.LIGHTBLUE_EX +"\n")
 
 
# Printing the Scoreboard
def print_scoreboard(score_board):
    print(Fore.MAGENTA +"\t|================================|")
    print(Fore.YELLOW +"\t   T H E  S C O R E   B O A R D    ")
    print(Fore.MAGENTA +"\t|================================|")
 
    players = list(score_board.keys())
    print(Fore.LIGHTGREEN_EX +"\t   ", players[0], "\t   |", score_board[players[0]])
    print(Fore.MAGENTA +"\t|--------------------------------|")
    print(Fore.LIGHTCYAN_EX +"\t   ", players[1], "\t   |", score_board[players[1]])
 
    print(Fore.MAGENTA +"\t|================================|\n")
# Function to check for the winner.
def check_win(player_pos, tic_tac_toe_player):
 
    # Combination of possible winnings
    possible_results = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in possible_results:
        if all(y in player_pos[tic_tac_toe_player] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       
 
# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
# Function for a single game of Tic Tac Toe
def single_game(tic_tac_toe_player):
 
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_game(values)
         
        # Try exception block for MOVE input
        try:
            print(Fore.LIGHTCYAN_EX +"Dear player with the game code", tic_tac_toe_player, " it's your turn now. Where are you placing your mark? : ", end="")
            move = int(input()) 
        except ValueError:
            print(Fore.RED +"Sorry, invalid Input!!! Try Again")
            time.sleep(1)
            continue
 
        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print(Fore.RED +"Sorry, invalid input!!! Try again by using numbers, '1 to 9'")
            time.sleep(1)
            continue
 
        # Check if the box is not occupied already
        if values[move-1] != ' ':
            print(Fore.RED +"Sorry, this place has been taken already. Try again someplace else!!")
            time.sleep(1)
            continue
 
        # Update game information
 
        # Updating grid status 
        values[move-1] = tic_tac_toe_player
 
        # Updating player positions
        player_pos[tic_tac_toe_player].append(move)
 
        # Function call for checking win
        if check_win(player_pos, tic_tac_toe_player):
            print_game(values)
            print(Fore.GREEN +"HOOORAY!!! Finnaly player with the game code", tic_tac_toe_player, " has WON the game... Congratulations!!")     
            time.sleep(1)
            print("\n")
            return tic_tac_toe_player
 
        # Function call for checking draw game
        if check_draw(player_pos):
            print_game(values)
            print(Fore.GREEN +"T I E !!! Seems no winner this Round, TOUGH GAME huh!!!")
            time.sleep(1)
            print("\n")
            return 'D'
 
        # Switch player moves
        if tic_tac_toe_player == 'X':
            tic_tac_toe_player = 'O'
        else:
            tic_tac_toe_player = 'X'
 
if __name__ == "__main__":
 
    print(Fore.YELLOW +"Dear First Player;")
    player1 = input(Fore.LIGHTGREEN_EX +"Please enter the your name here : ")
    print(Fore.LIGHTBLUE_EX +"\n")
 
    print(Fore.LIGHTMAGENTA_EX +"Dear Second  Player;")
    player2 = input(Fore.LIGHTCYAN_EX +"Kindly enter the your name here : ")
    print(Fore.LIGHTBLUE_EX +"\n")
     
    # Stores the player who chooses X and O
    tic_tac_toe_player = player1
 
    # Stores the choice of players
    player_choice = {'X' : "", 'O' : ""}
 
    # Stores the options
    options = ['X', 'O']
 
    # Stores the scoreboard
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit 
    while True:
 
        # Player choice Menu
        print(Fore.LIGHTGREEN_EX +"It's the time for", tic_tac_toe_player, "to decide;")
        print(Fore.YELLOW +"Dear", tic_tac_toe_player, "\nPlease Enter 1 to select the game code 'X'")
        print(Fore.LIGHTMAGENTA_EX +"Or just Enter 2 to select the game code 'O'")
        print(Fore.RED +"Otherwise, take some breath, enter 3 to Quit the Game and GO home.")
 
        # Try exception for CHOICE input
        try:
            choice = int(input())   
        except ValueError:
            print(Fore.RED +"Wrong Input!!! Please Try Again\n")
            continue
 
        # Conditions for player choice  
        if choice == 1:
            player_choice['X'] = tic_tac_toe_player
            if tic_tac_toe_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = tic_tac_toe_player
            if tic_tac_toe_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print(Fore.YELLOW +"\t       F i n a l  S c o r e s.")
            print_scoreboard(score_board)
            
            break  
 
        else:
            print(Fore.RED +"Wrong Choice!!!! PleaseTry Again\n")
 
        # Stores the winner in a single game of Tic Tac Toe
        winner = single_game(options[choice-1])
         
        # Edits the scoreboard according to the winner
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
            
 
        print_scoreboard(score_board)
        # Switch player who chooses X or O
        if tic_tac_toe_player == player1:
            tic_tac_toe_player = player2
        else:
            tic_tac_toe_player = player1
