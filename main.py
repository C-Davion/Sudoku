import tkinter as tk
import numpy as np
from copy import deepcopy
from typing import List, Optional


class Sudoku :
    def __init__(self,root):
         self.grid=[np.zeros((9,9), dtype=int)]
         self.current_grid_id=0
         self.root=root
         self.default_cell_color = 'white'
         self.selected_cell_color = "#82cdff"
    

    def setup(self): 
        for i in range(9):
            for j in range(9):
                   self.grid[self.current_grid_id][i][j]= (i//3 *3)+j//3 + 1


    def display(self):
        print(self.grid[self.current_grid_id])


    def GUI(self):
        self.root.title("Sudoku Grid")
        self.selected_cell = None  # To track the selected cell

        # Canvas-based grid for clean lines between cells
        self.cell_size = 50
        canvas_size = self.cell_size * 9
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=10)

        self.canvas = tk.Canvas(self.grid_frame, width=canvas_size, height=canvas_size, bg='white', highlightthickness=0)
        self.canvas.pack()

        # Draw cell separator lines (thin) and block separators (thicker)
        for i in range(10):
            width = 3 if i % 3 == 0 else 1
            # vertical
            x = i * self.cell_size
            self.canvas.create_line(x, 0, x, canvas_size, width=width, fill='black', tags=('grid_line',))
            # horizontal
            y = i * self.cell_size
            self.canvas.create_line(0, y, canvas_size, y, width=width, fill='black', tags=('grid_line',))

        # Prepare storage for text ids (None or int Tk canvas id)
        self.text_ids: List[List[Optional[int]]] = [[None for _ in range(9)] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                x = c * self.cell_size + self.cell_size // 2
                y = r * self.cell_size + self.cell_size // 2
                value = self.grid[self.current_grid_id][r][c]
                text = str(value) if value != 0 else ''
                tid = self.canvas.create_text(x, y, text=text, font=('Arial', 18), tags=('cell_text',))
                self.text_ids[r][c] = tid

        # Selection rectangle (hidden initially)
        self.selection_rect = None

        # Bind click on canvas to cell selection
        self.canvas.bind('<Button-1>', self._on_canvas_click)

        # Buttons for entering numbers
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=5)
        for n in range(1, 10):
            button = tk.Button(self.buttons_frame, text=str(n), command=lambda num=n: self.set_number(num), font=('Arial', 12))
            button.pack(side=tk.LEFT, padx=5)
        
        # Buttons for undo and redo
        button = tk.Button(self.buttons_frame, text="Undo", command=self.ctrl_z, font=('Arial', 12))
        button.pack(side=tk.LEFT, padx=5)
        button = tk.Button(self.buttons_frame, text="Redo", command=self.ctrl_y, font=('Arial', 12))
        button.pack(side=tk.LEFT, padx=5)
    

    def select_cell(self, row, col):
        """Handles cell selection."""
        # Remove previous selection rectangle
        if self.selection_rect is not None:
            self.canvas.delete(self.selection_rect)

        self.selected_cell = (row, col)
        x1 = col * self.cell_size
        y1 = row * self.cell_size
        x2 = (col + 1) * self.cell_size
        y2 = (row + 1) * self.cell_size
        # subtle fill to indicate selection while keeping grid lines visible
        self.selection_rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.selected_cell_color, outline='')
        
        # place the selection rectangle below the grid lines so lines remain visible
        try:
            self.canvas.tag_lower(self.selection_rect, 'grid_line')
        except Exception:
            pass
        print(f"Selected cell: {row}, {col}")


    def _on_canvas_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if 0 <= row < 9 and 0 <= col < 9:
            self.select_cell(row, col)
    
    
    def ctrl_z(self): #a modifier pour le boutton
        if self.current_grid_id > 0:
            self.current_grid_id -= 1
        else:
            pass
        self._refresh_canvas()


    def ctrl_y(self): #idem, a modifier pour le boutton
        if self.current_grid_id < len(self.grid) - 1:
            self.current_grid_id += 1
        else:  
            pass
            #display already at last step
        self._refresh_canvas()


    def set_number(self, value):
        """Change the value in the selected cell to the specified value."""
        if self.selected_cell is None:
            print("No cell selected!")
            return

        row, col = self.selected_cell
        new_grid=deepcopy(self.grid[self.current_grid_id])

        # Update the matrix
        new_grid[row][col] = value

        # drop the states if an undo happened, then append the new state
        self.grid = self.grid[:self.current_grid_id+1]
        self.grid.append(new_grid)
        self.current_grid_id += 1

        # refresh entire canvas from current grid
        self._refresh_canvas()


    def _refresh_canvas(self):
        # update all text items from the current grid
        grid = self.grid[self.current_grid_id]
        for r in range(9):
            for c in range(9):
                val = grid[r][c]
                self._update_cell_text(r, c, val)


    def _update_cell_text(self, r: int, c: int, val: int) -> None:
        """Update the canvas text for a single cell if the text id exists."""
        tid = self.text_ids[r][c]
        if tid is not None:
            self.canvas.itemconfigure(tid, text=str(val) if val != 0 else '')



class Workstate:
    def __init__(self):
        game_state=[] #tracks all moves
        curr_state=0 #


if __name__ == "__main__":
    root = tk.Tk()
    app = Sudoku(root)
    app.setup()
    app.display()
    app.GUI()
    root.mainloop()
    print("end")

