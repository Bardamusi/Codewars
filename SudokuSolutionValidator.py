"""
4 kyu - Sudoku Solution Validator

Sudoku Background

Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9,
so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks)
contain all of the digits from 1 to 9.

(More info at: http://en.wikipedia.org/wiki/Sudoku)
Sudoku Solution Validator

Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board,
and returns true if it is a valid solution, or false otherwise.
The cells of the sudoku board may also contain 0's, which will represent empty cells.
Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
"""

import numpy as np


def check_row(check_list, row):
    """
    :param check_list: the numbers we check against (so from 1-9)
    :param row: with integers from 0 - 9, with 0 indicating no number
    :return: Boolean True if is correct row, False else
    """
    freq_dict = {}
    for element in row:
        freq_dict[element] = freq_dict.get(element, 0) + 1

    for number in check_list:
        if freq_dict.get(number, 0) > 1:
            return False
    return True


def check_board(arr_board, lst):
    """
    :param arr_board: numpy array
    :param lst: values we check against
    :return: True or False depending if board is true along row/column
    """

    for row in arr_board:
        res = check_row(lst, row)
        if res is False:
            return False

    return True


def validSolution(board):
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = np.array(board)

    # Checks if the rows are correct
    if check_board(arr, check_list) is False:
        return False

    # Checks if the columns are correct (we use row operations since we transpose, so row here is column of board)
    if check_board(arr.T, check_list) is False:
        return False

    # Checks the 9 blocks of 3 by 3
    for i in range(0,9):
        r_i = i // 3
        col_i = i % 3
        helper = arr[(3*r_i):3*(r_i + 1), 3 * col_i: 3 * (col_i + 1)]
        if check_row(check_list, helper.flatten()) is False:
            return False

    return True


if __name__ == "__main__":

    print(validSolution([[5, 3, 4, 6, 7, 0, 0, 1, 2],
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

    print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                         [6, 7, 2, 1, 9, 0, 3, 4, 9],
                         [1, 0, 0, 3, 4, 2, 5, 6, 0],
                         [8, 5, 9, 7, 6, 1, 0, 2, 0],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 0, 1, 5, 3, 7, 2, 1, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 0, 0, 4, 8, 1, 1, 7, 9]]))

