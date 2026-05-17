import numpy as np




class SudokuSolver :
    def __init__(self, grid):
        self.grid = grid

    
    def is_cell_empty(self, i:int, j:int):
        return self.grid[i][j] == 0


    def row_is_valid(self, i:int):
        assert i<=8 and i>=0
        row = self.grid[i]
        numbers_in_row = set()
        for num in row:
            if num != 0:
                if num in numbers_in_row:
                    return False
                numbers_in_row.add(num)
        if 0 in row:
            return True
        return np.sum(row) == 45 and len(set(row)) == 9
    

    def column_is_valid(self, j:int):
        assert j<=8 and j>=0
        column = self.grid[:, j]
        numbers_in_column = set()
        for num in column:
            if num != 0:
                if num in numbers_in_column:
                    return False
                numbers_in_column.add(num)
        if 0 in column:
            return True
        return np.sum(column) == 45 and len(set(column)) == 9

    def three_by_three_is_valid(self, i:int):
        
        '''
        The three by three are numbered as follows:
        0 1 2
        3 4 5
        6 7 8
        '''
        assert i<=8 and i>=0
        temp=[] #to gather the respective element in the grid
        index_i,index_j= i//3, i%3 #get which three by three it is
        for m in range (index_i*3,index_i*3+3): #get the rows index
            for n in range(index_j*3,index_j*3+3): #get the col index
                temp.append(self.grid[m,n])
        if 0 in temp:
            return True
        return np.sum(np.array(temp))==45 and len(set(temp))==9



    def sudoku_is_valid(self):
        for i in range(9):
            if not self.row_is_valid(i) or not self.column_is_valid(i) or not self.three_by_three_is_valid(i):
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