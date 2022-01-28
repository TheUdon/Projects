import random as rand
import time

current_turn = 1

# The Tic Tac Toe board is set up to mimic the numpad on a keyboard so it is a bit more intuitive
def make_board(inputs):
    print("\n\t     |     |")
    print("\t  {}  |  {}  |  {}".format(inputs[6], inputs[7], inputs[8]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(inputs[3], inputs[4], inputs[5]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(inputs[0], inputs[1], inputs[2]))
    print("\t     |     |")
    print("\n")


def coin_flip():
    coin_flip = rand.randint(0, 1)
    if coin_flip == 0:
        player1_order = 1
        print("Player 1 goes first")
        return player1_order
    else:
        player1_order = 2
        print("Player 2 goes first")
        return player1_order

def x_or_o():
    coin_flip = rand.randint(0, 1)
    if coin_flip == 0:
        print("Player 1 is X and Player 2 is O")
        player1_char = "X"
        return player1_char
    else:
        print("Player 1 is O and Player 2 is X")
        player1_char = "O"
        return player1_char


def comp_turn(spaces_left, cpu_x_o):
    global player_plays
    print("The CPU is thinking...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    cpu_decide = rand.choice(spaces_left)
    spaces.remove(cpu_decide)
    plays[cpu_decide - 1] = cpu_x_o
    filled_space.append(cpu_decide)
    player_plays[2].append(cpu_decide)


def turn(cpu_on, player1_order, player1_x_or_o):
    global filled_space
    global current_turn
    if player1_x_or_o == "X":
        player2_x_or_o = "O"
    else:
        player2_x_or_o = "X"

    if player1_order == 1:
        if current_turn % 2 == 0:
            player1_decide = int(input(f"Which space number would you like to place an {player1_x_or_o}? "))
            legal_move = False
            while legal_move is False:
                if player1_decide in filled_space:
                    player1_decide = int(input("That space has already been filled, please type in a different space: "))
                elif player1_decide > 9 or player1_decide < 1:
                    player1_decide = int(input("That is an invalid entry, please type in a different space: "))
                else:
                    legal_move = True
            filled_space.append(player1_decide)
            spaces.remove(player1_decide)
            plays[player1_decide-1] = player1_x_or_o
            player_plays[1].append(player1_decide)
        else:
            if cpu_on is True:
                comp_turn(spaces, player2_x_or_o)
            else:
                player2_decide = int(input(f"Which space number would you like to place an {player2_x_or_o}? "))
                legal_move = False
                while legal_move is False:
                    if player2_decide in filled_space:
                        player2_decide = int(
                            input("That space has already been filled, please type in a different space: "))
                    elif player2_decide > 9 or player2_decide < 1:
                        player2_decide = int(input("That is an invalid entry, please type in a different space: "))
                    else:
                        legal_move = True
                filled_space.append(player2_decide)
                spaces.remove(player2_decide)
                plays[player2_decide - 1] = player2_x_or_o
                player_plays[2].append(player2_decide)

    else:
        if current_turn % 2 == 0:
            if cpu_on is True:
                comp_turn(spaces, player2_x_or_o)
            else:
                player2_decide = int(input(f"Which space number would you like to place an {player2_x_or_o}? "))
                legal_move = False
                while legal_move is False:
                    if player2_decide in filled_space:
                        player2_decide = int(
                            input("That space has already been filled, please type in a different space: "))
                    elif player2_decide > 9 or player2_decide < 1:
                        player2_decide = int(input("That is an invalid entry, please type in a different space: "))
                    else:
                        legal_move = True
                filled_space.append(player2_decide)
                spaces.remove(player2_decide)
                plays[player2_decide - 1] = player2_x_or_o
                player_plays[2].append(player2_decide)

        else:
            player1_decide = int(input(f"Which space number would you like to place an {player1_x_or_o}? "))
            legal_move = False
            while legal_move is False:
                if player1_decide in filled_space:
                    player1_decide = int(
                        input("That space has already been filled, please type in a different space: "))
                elif player1_decide > 9 or player1_decide < 1:
                    player1_decide = int(input("That is an invalid entry, please type in a different space: "))
                else:
                    legal_move = True
            filled_space.append(player1_decide)
            spaces.remove(player1_decide)
            plays[player1_decide - 1] = player1_x_or_o
            player_plays[1].append(player1_decide)


def check_win(players_moves, turn_order):
    global current_turn
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    if len(players_moves[1]) + len(players_moves[2]) == 9:
        print("Draw. You tied with each other.")
        make_board(plays)
        return

    if turn_order == 1:
        if current_turn % 2 == 0:
            for x in wins:
                win = all(y in players_moves[1] for y in x)
                if win:
                    print("Player 1 wins!")
                    make_board(plays)
                    current_turn = 9
                    return current_turn
        else:
            for x in wins:
                win = all(y in players_moves[2] for y in x)
                if win:
                    print("Player 2 wins!")
                    make_board(plays)
                    current_turn = 9
                    return current_turn
    else:
        if current_turn % 2 == 0:
            for x in wins:
                win = all(y in players_moves[2] for y in x)
                if win:
                    print("Player 2 wins!")
                    make_board(plays)
                    current_turn = 9
                    return current_turn
        else:
            for x in wins:
                win = all(y in players_moves[1] for y in x)
                if win:
                    print("Player 1 wins!")
                    make_board(plays)
                    current_turn = 9
                    return current_turn

spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
make_board(spaces)
game_on = input("Would you like to play a game of Tic-Tac-Toe?\n'Yes' or 'No': ")
if game_on.upper() == 'YES':
    game_on = True
else:
    game_on = False

vs_cpu = input("Would you like to play against the computer or another person?\nPlease type either 'CPU' or 'Player': ")
if vs_cpu.upper() != "PLAYER" and vs_cpu.upper() != "CPU":
    valid_entry = False
else:
    valid_entry = True
while valid_entry is False:
    vs_cpu = input("That was an invalid entry\nPlease type either 'CPU' or 'Player': ")
    if vs_cpu.upper() != "PLAYER" and vs_cpu.upper() != "CPU":
        valid_entry = False
    else:
        valid_entry = True


if vs_cpu.upper() == "CPU":
    cpu = True
else:
    cpu = False

print("Flipping coin to see who goes first...")
time.sleep(1)
print("...")
time.sleep(1)
player1_turn_order = coin_flip()
x_o = x_or_o()

filled_space = []
plays = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player_plays = {1: [],
                2: []}

while game_on:
    make_board(plays)
    turn(cpu, player1_turn_order, x_o)
    check_win(player_plays, player1_turn_order)
    current_turn += 1
    if current_turn == 10:
        game_on = input("Would you like to play again?\n'Yes' or 'No': ")
        if game_on.upper() == "YES":
            current_turn = 0
            filled_space = []
            spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            plays = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            player_plays = {1: [],
                            2: []}
            game_on = True
        else:
            print("Thank you for playing!")
            game_on = False