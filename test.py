# Initialize the board as 0s (empty cells)
board = [[0 for _ in range(3)] for _ in range(3)]

# Player symbols: 'X' and 'O'
players = ['X', 'O']

while True:
    # Print current state of the board
    print("Current Board:")
    for row in board:
        print(row, end=" ")

    # Check if any player has won
    winner = None
    for i in range(3):
        if all(board[i][j] == players[0] for j, j_val in enumerate(board[i])):
            winner = i
            break

    if winner is not None:
        print(f"\nPlayer {players[winner]} wins!")
        break

    # Check rows
    for row in board:
        if all(cell == players[0] for cell in row):
            winner = row.index(players[0])
            print(f"\nPlayer {players[winner]} wins!")
            break

    # Check columns
    for col in range(3):
        if all(board[row][col] == players[0] for row, row_val in enumerate(board)):
            winner = col
            print(f"\nPlayer {players[winner]} wins!")
            break

    # Check diagonals
    if all(board[i][i] == players[0] for i in range(3)):
        winner = 2
        print(f"\nPlayer {players[winner]} wins!")
        break

    # Try next player's turn
    if winner is None:
        board[board.index(0) + 1] = 0

# Game ends without a winner, it's a draw!
print("\nGame ended in a draw!")