"""
Battle royale game launch
Write a program that reads in a selected game mode and calls one of two functions to launch the game. 
If the input is "br", call battle_royale(). Otherwise, call practice().
"""

def find_teammates(num):
    print("Finding", num, "players...")

# Define battle_royale() and practice()
def battle_royale():
    players = int(input('Enter number of players: '))
    num = 3 - players
    find_teammates(num)
    print('Match starting.....')
    
def practice():
    desired_map = input('Enter desired map: ')
    print('Launching practice on', desired_map)
    

game_mode = input()
# Launch selected game mode
if game_mode == 'br':
    battle_royale()
elif game_mode == 'p':
    practice()