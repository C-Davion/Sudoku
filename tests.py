import numpy as np 
from solve import SudokuSolver



def test_row_is_valid():
    grid = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [5, 5, 5, 5, 5, 5, 5, 5, 5],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0 ,1],
                     [9 ,8 ,7 ,6 ,5 ,4 ,3 ,2 ,1]])
    solver = SudokuSolver(grid)
    assert solver.row_is_valid(1) == True
    assert solver.row_is_valid(5) == False
    assert solver.row_is_valid(7) == False  ### Trucs à corriger pck on a 2 fois le chiffre 1, dans le fichier solve.py
    assert solver.row_is_valid(8) == True


def test_placeable_digits():
    grid = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 5 ,5 ,5 ,5 ,5],
                     [5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5],
                     [0 ,0 ,0 ,0 ,0 ,0 ,1 ,2 ,3],
                     [9 ,8 ,7 ,6 ,5 ,4 ,3 ,2 ,1],
                     [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]])
    solver = SudokuSolver(grid)
    print(solver.placeable_digits(1,1))
    print(solver.placeable_digits(4,4))
    print(solver.placeable_digits(6,6))


if __name__ == "__main__":
    test_row_is_valid()
    test_placeable_digits()