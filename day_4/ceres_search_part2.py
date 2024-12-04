def check_x(board, y, x):
    if x + 1 >= len(board[0]) or x - 1 < 0 or y - 1 < 0 or y + 1 >= len(board):
        return False
    diagonal_1 = [board[y - 1][x - 1], board[y + 1][x + 1]]
    diagonal_2 = [board[y - 1][x + 1], board[y + 1][x - 1]]
    if (
        "M" in diagonal_1
        and "S" in diagonal_1
        and "M" in diagonal_2
        and "S" in diagonal_2
    ):
        return True


with open("day_4/input2.txt", "r") as file:
    board = [list(line.strip()) for line in file.readlines()]
    total_count = 0

    for y, row in enumerate(board):
        for x, column in enumerate(row):
            if column == "A" and check_x(board, y, x):
                total_count += 1
    print(total_count)