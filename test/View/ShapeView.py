import tkinter as tk
class ShapeView(tk.Label):
    def __init__(self, parent, model):
        super().__init__(parent, bg=model.color, width=model.width, height=model.height)
        self.place(x=model.x, y=model.y)