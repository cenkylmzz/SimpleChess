values_of_pieces = {"P": 1, "R": 5, "N": 3, "B": 3, "Q": 9, "K": 999,
                    "p": -1, "r": -5, "n": -3, "b": -3, "q": -9, "k": -999, "-": 0}

chess_board = {"a1": "R", "b1": "N", "c1": "B", "d1": "Q", "e1": "K", "f1": "B", "g1": "N", "h1": "R",
               "a2": "P", "b2": "P", "c2": "P", "d2": "P", "e2": "P", "f2": "P", "g2": "P", "h2": "P",
               "a3": "-", "b3": "-", "c3": "-", "d3": "-", "e3": "-", "f3": "-", "g3": "-", "h3": "-",
               "a4": "-", "b4": "-", "c4": "-", "d4": "-", "e4": "-", "f4": "-", "g4": "-", "h4": "-",
               "a5": "-", "b5": "-", "c5": "-", "d5": "-", "e5": "-", "f5": "-", "g5": "-", "h5": "-",
               "a6": "-", "b6": "-", "c6": "-", "d6": "-", "e6": "-", "f6": "-", "g6": "-", "h6": "-",
               "a7": "p", "b7": "p", "c7": "p", "d7": "p", "e7": "p", "f7": "p", "g7": "p", "h7": "p",
               "a8": "r", "b8": "n", "c8": "b", "d8": "q", "e8": "k", "f8": "b", "g8": "n", "h8": "r"}


def printing_chess_board():
    for j in range(8, 0, -1):
        print(j, chess_board["a" + str(j)], chess_board["b" + str(j)], chess_board["c" + str(j)],
              chess_board["d" + str(j)], chess_board["e" + str(j)], chess_board["f" + str(j)],
              chess_board["g" + str(j)], chess_board["h" + str(j)])
    print("  a b c d e f g h")

def is_valid_move(move, board, player):
    # Check if move is in the format of 'a1b2'
    if len(move) != 4:
        return False
    piece_column, piece_row, new_column, new_row = move[0], move[1], move[2], move[3]

    # Check if piece exists in the starting position
    if board[piece_column + piece_row] == "-":
        return False

    # Check if piece belongs to the player whose turn it is
    piece_value = values_of_pieces[board[piece_column + piece_row]]
    if piece_value > 0 and player == "black":
        return False
    if piece_value < 0 and player == "white":
        return False

    # Check if destination is a valid square on the board
    if new_column not in "abcdefgh" or new_row not in "12345678":
        return False

    # Check if destination is not occupied by a piece of the same player
    if board[new_column + new_row] != "-" and \
            (piece_value > 0 and values_of_pieces[board[new_column + new_row]] > 0 or
             piece_value < 0 and values_of_pieces[board[new_column + new_row]] < 0):
        return False

    # Check if the move is valid for the given piece type
    if board[piece_column + piece_row].lower() == "p":
        # Check if pawn is making a double move from the starting position
        if (player == "white" and piece_row == "2" and new_row == "4") or \
                (player == "black" and piece_row == "7" and new_row == "5"):
            if piece_column != new_column:
                return False
            if board[new_column + new_row] != "-":
                return False
            return True
        # Check if pawn move is in correct direction
        if (player == "white" and int(new_row) - int(piece_row) != 1) or \
                (player == "black" and int(new_row) - int(piece_row) != -1):
            return False
        # Check if pawn is moving forward without capturing
        if piece_column == new_column and board[new_column + new_row] != "-":
            return False
        # Check if pawn is capturing a piece diagonally
        if abs(ord(new_column) - ord(piece_column)) == 1 and board[new_column + new_row] == "-":
            return False

    elif board[piece_column + piece_row].lower() == "r":
        # Check if rook is moving horizontally or vertically without obstruction
        if piece_column != new_column and piece_row != new_row:
            return False
        if piece_column == new_column:
            start, end = min(int(piece_row), int(new_row)), max(int(piece_row), int(new_row))
            for i in range(start + 1, end):
                if board[piece_column + str(i)] != "-":
                    return False
        elif piece_row == new_row:
            start, end = min(ord(piece_column), ord(new_column)), max(ord(piece_column), ord(new_column))
            for i in range(start + 1, end):
                if board[chr(i) + piece_row] != "-":
                    return False
    elif board[piece_column + piece_row].lower() == "n":
        # Check if knight is moving in an L-shape without obstruction
        column_diff = abs(ord(new_column) - ord(piece_column))
        row_diff = abs(int(new_row) - int(piece_row))
        if not ((column_diff == 2 and row_diff == 1) or (column_diff == 1 and row_diff == 2)):
            return False
    elif board[piece_column + piece_row].lower() == "b":
        # Check if bishop is moving diagonally without obstruction
        if abs(ord(new_column) - ord(piece_column)) != abs(int(new_row) - int(piece_row)):
            return False
        column_direction = 1 if ord(new_column) > ord(piece_column) else -1
        row_direction = 1 if int(new_row) > int(piece_row) else -1
        column = ord(piece_column) + column_direction
        row = int(piece_row) + row_direction
        while column != ord(new_column) and row != int(new_row):
            if board[chr(column) + str(row)] != "-":
                return False
            column += column_direction
            row += row_direction
    elif board[piece_column + piece_row].lower() == "q":
        # Check if queen is moving diagonally or horizontally/vertically without obstruction
        if piece_column != new_column and piece_row != new_row:
            if abs(ord(new_column) - ord(piece_column)) != abs(int(new_row) - int(piece_row)):
                return False
            column_direction = 1 if ord(new_column) > ord(piece_column) else -1
            row_direction = 1 if int(new_row) > int(piece_row) else -1
            column = ord(piece_column) + column_direction
            row = int(piece_row) + row_direction
            while column != ord(new_column) and row != int(new_row):
                if board[chr(column) + str(row)] != "-":
                    return False
                column += column_direction
                row += row_direction
        else:
            start, end = min(int(piece_row), int(new_row)), max(int(piece_row), int(new_row))
            for i in range(start + 1, end):
                if piece_column == new_column:
                    if board[piece_column + str(i)] != "-":
                        return False
                else:
                    if board[chr(ord(piece_column) + (1 if ord(new_column) > ord(piece_column) else -1) * (i - int(piece_row))) + str(i)] != "-":
                        return False
    elif board[piece_column + piece_row].lower() == "k":
        # Check if king is moving to an adjacent square
        if abs(ord(new_column) - ord(piece_column)) > 1 or abs(int(new_row) - int(piece_row)) > 1:
            return False
    else:
        return False
    return True

score = 0
printing_chess_board()
turn = "white"
print("White's turn")
while True:
    a = input()
    piece_column_piece_row = a[0:2]
    new_column_new_row = a[2:4]
    if not is_valid_move(a, chess_board, turn):
        print("Invalid Move!")
    else:
        score = score - values_of_pieces[chess_board[new_column_new_row]]
        chess_board.update({new_column_new_row: chess_board[piece_column_piece_row]})
        chess_board.update({piece_column_piece_row: "-"})
        if turn == "black":
            turn = "white"
        else:
            turn = "black"
        printing_chess_board()
    print("SCORE :", score)
    if score > 900 or score < -900:
        if turn == "black":
            print("GAME OVER!")
            print("WHITE WON!")
        if turn == "white":
            print("GAME OVER!")
            print("BLACK WON!")
        break

    if turn == "black":
        print("Black's turn")
    else:
        print("White's turn")