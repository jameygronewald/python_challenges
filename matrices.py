winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

test_board = [[2, 0, 2],
	[0, 2, 1],
	[2, 0, 0]]

def evaluate_board(board):
    if board[0][0] == board [1][1] == board[2][2]:
        match = board[0][0]
        if match != 0:
            print(f"Player {match} wins!")
    if board[2][0] == board [1][1] == board[0][2]:
        match = board[2][0]
        if match != 0:
            print(f"Player {match} wins!")
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            match = board[i][0]
            if match != 0:
                print(f"Player {match} wins!")
        if board[0][i] == board[1][i] == board[2][i]:
            match = board[0][i]
            if match != 0:
                print(f"Player {match} wins!")

print('test1')
evaluate_board(winner_is_2)
print('test2')
evaluate_board(winner_is_1)
print('test3')
evaluate_board(winner_is_also_1)
print('test4')
evaluate_board(no_winner)
print('test5')
evaluate_board(also_no_winner)
print('test_board')
evaluate_board(test_board)