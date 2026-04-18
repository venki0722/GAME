import random

def init_board():
    nums = list(range(1, 16)) + [" "]
    random.shuffle(nums)
    return [nums[i:i+4] for i in range(0, 16, 4)]

def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == " ":
                return i, j

def move(board, i, j):
    empty_i, empty_j = find_empty(board)

    if abs(empty_i - i) + abs(empty_j - j) == 1:
        board[empty_i][empty_j], board[i][j] = board[i][j], board[empty_i][empty_j]

def is_solved(board):
    correct = list(range(1, 16)) + [" "]
    flat = sum(board, [])
    return flat == correct
