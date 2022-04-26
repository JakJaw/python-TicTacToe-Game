def game():
    def check_turn(turn):
        if (turn % 2) == 0:
            return "X"
        else:
            return "O"

    def display_board():
        print("\n" + board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
        print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
        print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9" + "\n")

    def is_empty(place, a, b, turn):
        if place in a or place in b:
            print("place is not empty!!!")
            return False
        else:
            return True

    def add_to_list(player):
        if player == "X":
            return player_x_moves.append(player_input)
        else:
            return player_o_moves.append(player_input)

    def check_if_winner(player, turn):
        if board[0] == board[1] == board[2] != " ":
            print(f"player {player} wins!!!")
            return True
        if board[3] == board[4] == board[5] != " ":
            print(f"player {player} wins!!!")
            return True
        if board[6] == board[7] == board[8] != " ":
            print(f"player {player} wins!!!")
            return True
        if board[0] == board[3] == board[6] != " ":
            print(f"player {player} wins!!!")
            return True
        if board[1] == board[4] == board[7] != " ":
            print(f"player {player} wins!!!")
            return True
        if board[2] == board[5] == board[8] != " ":
            print(f"player {player} wins!!!")
            return True
        if board[0] == board[4] == board[8] != " ":
            print(f"player {player} wins!!!")
            return True
        if board[2] == board[4] == board[6] != " ":
            print(f"player {player} wins!!!")
            return True
        if turn == 9:
            print("It's a draw...")
            return True
        else:
            return False

    def again():
        play_again = str(input("Wanna play again? (Y/N): ")).upper()
        if play_again == "N":
            return True
        else:
            return False

    is_on = True
    print("Welcome in Tic Tac Toe game")

    while is_on:
        in_game = True
        winner = False
        player = ""
        turn = 1
        board = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]
        player_o_moves = []
        player_x_moves = []

        while in_game:
            display_board()
            player_input = int(input("Enter the place: "))

            if is_empty(player_input, player_o_moves, player_x_moves, turn):
                player = check_turn(turn)
                add_to_list(player)
                board[player_input - 1] = player
                winner = check_if_winner(player, turn)
                turn += 1
            if winner:
                display_board()
                if again():
                    is_on = False
                    in_game = False
                else:
                    in_game = False


game()
print("Goodbye...")
