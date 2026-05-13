import numpy as np




class SudokuSolver :
    def __init__(self, grid):
        self.grid = grid

    
    def is_cell_empty(self, i, j):
        return self.grid[i][j] == 0

### ici il y a des choses à changer ###
    def row_is_valid(self, i):
        row = self.grid[i]
        if 0 in row:
            return True
        return np.sum(row) == 45 and len(set(row)) == 9
    

    def column_is_valid(self, j):
        column = self.grid[:, j]
        if 0 in column:
            return True
        return np.sum(column) == 45 and len(set(column)) == 9

### fin des choses à changer ###


    def sudoku_is_valid(self):
        for i in range(9):
            if not self.row_is_valid(i) or not self.column_is_valid(i):
                return False
        return True
    

    def placeable_digits(self, i, j):
        if not self.is_cell_empty(i, j):
            return set()  
        
        digits = set(range(1, 10))
        digits_copy = digits.copy()
        
        for digit in digits:
            if digit in self.grid[i]:  # Check row
                digits_copy.remove(digit)
            if digit in self.grid[:, j]:  # Check column
                digits_copy.remove(digit)
        
        return digits_copy

'''
    def brute_force(self):
        for i in range (9):
            for j in range(9):
                if self.grid[i][j] == 0:

'''

if __name__ == "__main__":
    print("Hello world")