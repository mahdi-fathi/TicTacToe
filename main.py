def draw_board(board: list[list[str]]) -> None:
    for row in board:
        for cell in row:
            if cell is row[-1]:
                print(f" {cell} ")
            else:
                print(f" {cell} |", end="")
    # for row_num in range(len(board)):
    #     for col_num in range(len(board[row_num])):
    #         if col_num == len(board) - 1:
    #             print(f" {board[row_num][col_num]} ")
    #         else:
    #             print(f" {board[row_num][col_num]} |", end='')


def tictactoe(board: list[list[str]]):
    draw_board(board)


def main():
    lst = [['X', 'O', ' '], [' ', 'X', 'O'], ['O', ' ', ' ']]
    # while True:
    draw_board(lst)


if __name__ == "__main__":
    main()
