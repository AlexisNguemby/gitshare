def draw_board(board):
    print(f"{board[7]}|{board[8]}|{board[9]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[1]}|{board[2]}|{board[3]}")

def winner(board, player):
    combinations = [(7,8,9), (4,5,6), (1,2,3), (7,4,1), (8,5,2), (9,6,3), (7,5,3), (9,5,1)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in combinations)

def tic_tac_toe():
    board, player = [' '] * 10, 'X'
    for _ in range(9):
        draw_board(board)
        try:
            choice = int(input(f"Player {player}, choose a spot (1-9): "))
            if board[choice] != ' ': raise ValueError
            board[choice] = player
            if winner(board, player):
                draw_board(board)
                print(f"Congratulations! Player {player} wins!")
                return
            player = 'O' if player == 'X' else 'X'
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")
    draw_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
