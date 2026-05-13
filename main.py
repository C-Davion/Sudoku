import tkinter as tk
import numpy as np


class Sudoku :
    def __init__(self,root):
         self.grid=np.zeros((9,9), dtype=int)
         self.root=root
         self.default_cell_color = 'white'
         self.selected_cell_color = "#82cdff"
    

    def setup(self): 
        for i in range(9):
            for j in range(9):
                   self.grid[i][j]= (i//3 *3)+j//3 + 1

    def display(self):
        print(self.grid)

    def GUI(self):
        self.root.title("Sudoku Grid")
        
        
        self.selected_cell = None  # To track the selected cell
        
        # Create a frame for the grid
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=5)
        
        # Create a grid of Entry widgets
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(
                    self.grid_frame,
                    width=4,
                    justify='center',
                    font=('Arial', 14),
                    bg=self.default_cell_color,
                    highlightthickness=0,
                    cursor='arrow'
                )
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, str(self.grid[i][j]))

                # Prevent manual typing while keeping the widget clickable.
                entry.bind("<Key>", lambda e: "break")
                
                # Add click event to select the cell; return 'break' to prevent focus (hides caret)
                entry.bind("<1>", lambda e, row=i, col=j: (self.select_cell(row, col), 'break')[1])
                
                self.entries[i][j] = entry
        

        for n in range (1, 10):
            button = tk.Button(self.buttons_frame, text=str(n), command=lambda num=n: self.set_number(num), font=('Arial', 12))
            button.pack(side=tk.LEFT, padx=5)
    
    def select_cell(self, row, col):
        """Handles cell selection."""
        if self.selected_cell is not None:
            prev_row, prev_col = self.selected_cell
            self.entries[prev_row][prev_col].config(bg=self.default_cell_color)

        self.selected_cell = (row, col)
        self.entries[row][col].config(bg=self.selected_cell_color)
        print(f"Selected cell: {row}, {col}")  # For debugging purposes
    
    def set_number(self, value):
        """Change the value in the selected cell to the specified value."""
        if self.selected_cell is not None:
            row, col = self.selected_cell
            
            # Update the matrix
            self.grid[row][col] = value
            
            # Reflect the change in the corresponding entry widget
            self.entries[row][col].delete(0, tk.END)
            self.entries[row][col].insert(0, str(value))
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

