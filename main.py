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
            self.canvas.create_line(x, 0, x, canvas_size, width=width, fill='black')
            # horizontal
            y = i * self.cell_size
            self.canvas.create_line(0, y, canvas_size, y, width=width, fill='black')

        # Prepare storage for text ids
        self.text_ids = [[None for _ in range(9)] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                x = c * self.cell_size + self.cell_size // 2
                y = r * self.cell_size + self.cell_size // 2
                value = self.grid[r][c]
                text = str(value) if value != 0 else ''
                tid = self.canvas.create_text(x, y, text=text, font=('Arial', 18))
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
    

    def select_cell(self, row, col):
        """Handles cell selection."""
        # Remove previous selection rectangle
        if self.selection_rect is not None:
            self.canvas.delete(self.selection_rect)

        self.selected_cell = (row, col)
        x1 = col * self.cell_size + 1
        y1 = row * self.cell_size + 1
        x2 = (col + 1) * self.cell_size - 1
        y2 = (row + 1) * self.cell_size - 1
        # subtle fill to indicate selection while keeping grid lines visible
        self.selection_rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.selected_cell_color, outline='')
        # ensure numbers are visible above the selection
        for r in range(9):
            for c in range(9):
                self.canvas.tag_raise(self.text_ids[r][c])
        print(f"Selected cell: {row}, {col}")


    def _on_canvas_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if 0 <= row < 9 and 0 <= col < 9:
            self.select_cell(row, col)
    

    def set_number(self, value):
        """Change the value in the selected cell to the specified value."""
        if self.selected_cell is None:
            print("No cell selected!")
            return

        row, col = self.selected_cell
        # Update the matrix
        self.grid[row][col] = value
        # Update canvas text
        tid = self.text_ids[row][col]
        self.canvas.itemconfigure(tid, text=str(value) if value != 0 else '')


### faire le bouton controle z ici ###
class Workstate:
    def __init__(self):
        print("Hello World")


if __name__ == "__main__":
    root = tk.Tk()
    app = Sudoku(root)
    app.setup()
    app.display()
    app.GUI()
    root.mainloop()
    print("end")
    app.display()

