def horizontal(board):
    count = 0
    for row in board:
        row_str = "".join(row)
        count += row_str.count("XMAS") + row_str.count("SAMX")
    return count


def bottom_right_diagonal(board, y, x):
    if x + 3 >= len(board[0]) or y + 3 >= len(board):
        return False
    return (
        board[y + 1][x + 1] == "M"
        and board[y + 2][x + 2] == "A"
        and board[y + 3][x + 3] == "S"
    )


def bottom_left_diagonal(board, y, x):
    if x - 3 < 0 or y + 3 >= len(board):
        return False
    return (
        board[y + 1][x - 1] == "M"
        and board[y + 2][x - 2] == "A"
        and board[y + 3][x - 3] == "S"
    )


def top_right_diagonal(board, y, x):
    if x + 3 >= len(board[0]) or y - 3 < 0:
        return False
    return (
        board[y - 1][x + 1] == "M"
        and board[y - 2][x + 2] == "A"
        and board[y - 3][x + 3] == "S"
    )


def top_left_diagonal(board, y, x):
    if x - 3 < 0 or y - 3 < 0:
        return False
    return (
        board[y - 1][x - 1] == "M"
        and board[y - 2][x - 2] == "A"
        and board[y - 3][x - 3] == "S"
    )


def check_diagonals(board, y, x):
    count = 0
    if top_left_diagonal(board, y, x):
        count += 1
    if top_right_diagonal(board, y, x):
        count += 1
    if bottom_left_diagonal(board, y, x):
        count += 1
    if bottom_right_diagonal(board, y, x):
        count += 1
    return count


def rotate(board):
    rows, cols = len(board), len(board[0])
    new_board = [[board[rows - 1 - i][j] for i in range(rows)] for j in range(cols)]
    return new_board


with open("day_4/input.txt", "r") as file:
    board = [list(line.strip()) for line in file.readlines()]
    total_count = 0

    for y, row in enumerate(board):
        for x, column in enumerate(row):
            if column == "X":
                total_count += check_diagonals(board, y, x)

    total_count += horizontal(board)
    total_count += horizontal(rotate(board))
    print(total_count)