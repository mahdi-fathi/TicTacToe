import random
from pyfiglet import Figlet
import os


def get_input() -> str:
    inp = input("\nenter the num: ")
    if inp in [str(i) for i in range(1, 10)]:
        return inp
    else:
        raise IndexError


def check_win(board: list[list[str]]) -> int:
    """ 0: game not ended
        1: user1 (X) won
        2: user2 (O) won
        3: draw"""
    for row_num in range(len(board)):
        if board[row_num][0] == board[row_num][1] == board[row_num][2] != " ":
            return 1 if board[row_num][0] == "X" else 2
        for col_num in range(len(board[0])):
            if board[0][col_num] == board[1][col_num] == board[2][col_num] != ' ':
                return 1 if board[0][col_num] == "X" else 2
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return 1 if board[0][0] == "X" else 2
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return 1 if board[0][2] == "X" else 2
    if all(all(cell != " " for cell in row) for row in board):
        return 3
    return 0


def process_input(board: list[list[str]], user: int) -> None:
    input_ = ''
    input_book = {"1": (2, 0), "2": (2, 1), "3": (2, 2),
                  "4": (1, 0), "5": (1, 1), "6": (1, 2),
                  "7": (0, 0), "8": (0, 1), "9": (0, 2), }
    while not input_:
        try:
            input_ = get_input()
            row, col = input_book.get(input_, (0, 0))
            if board[row][col] == "X" or board[row][col] == "O":
                raise IndexError
            board[row][col] = 'X' if user == 0 else 'O'
            break

        except IndexError:
            input_ = ''


def draw_board(board: list[list[str]]) -> None:
    # for row in board:
    #     for cell in row:
    #         if cell is row[-1]:
    #             print(f" {cell} ")
    #         else:
    #             print(f" {cell} |", end="")
    for row_num in range(len(board)):
        for col_num in range(len(board[row_num])):
            if col_num == len(board) - 1:
                print(f" {board[row_num][col_num]} ")
            else:
                print(f" {board[row_num][col_num]} |", end='')





def tictactoe(board: list[list[str]]):
    user = 0
    draw_board(board)
    while check_win(board) == 0:
        process_input(board, user)
        os.system('cls')
        draw_board(board)
        user += 1
        user %= 2


def main():
    # lst = [[" " for i in range(3)] for j in range(3)]
    lst = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    tictactoe(lst)


if __name__ == "__main__":
    main()
