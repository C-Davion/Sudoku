import tkinter as tk
import numpy as np


class Sudoku :
    def __init__(self,root):
         self.grid=np.zeros((9,9))
         self.root=root
    

    def setup(self): 
        for i in range(9):
            for j in range(9):
                   self.grid[i][j]=(i//3 *3)+j//3

    def display(self):
        print(self.grid)

    def GUI(self):
        self.root.title("Sudoku Grid")
        
        
        self.selected_cell = None  # To track the selected cell
        
        # Create a frame for the grid
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=10)
        
        # Create a grid of Entry widgets
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.grid_frame, width=4, justify='center', font=('Arial', 14))
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, str(self.grid[i][j]))
                
                # Add click event to select the cell
                entry.bind("<Button-1>", lambda e, row=i, col=j: self.select_cell(row, col))
                
                self.entries[i][j] = entry
        
        # Create a button to subtract 1
        self.subtract_button = tk.Button(self.root, text="-1", command=self.subtract_one, font=('Arial', 14))
        self.subtract_button.pack(pady=5)
    
    def select_cell(self, row, col):
        """Handles cell selection."""
        self.selected_cell = (row, col)
        print(f"Selected cell: {row}, {col}")  # For debugging purposes
    
    def subtract_one(self):
        """Subtract 1 from the value in the selected cell."""
        if self.selected_cell is not None:
            row, col = self.selected_cell
            
            # Update the matrix
            self.grid[row][col] -= 1
            
            # Reflect the change in the corresponding entry widget
            self.entries[row][col].delete(0, tk.END)
            self.entries[row][col].insert(0, str(self.grid[row][col]))
        else:
            print("No cell selected!")



if __name__ == "__main__":
    root = tk.Tk()
    app = Sudoku(root)
    app.setup()
    app.display()
    app.GUI()
    root.mainloop()
    print("end")
    app.display()

