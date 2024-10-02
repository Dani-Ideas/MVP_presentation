from View.ShapeView import ShapeView
from Model.DraggableObject import ShapeModel
from Controller.DragController import ShapeController
from tkinter import *
window = Tk()
window.geometry("720x520")

# Crear modelos
square_model = ShapeModel(0, 0, 10, 5, "blue")
square2_model = ShapeModel(100, 100, 10, 5, "red")
square3_model = ShapeModel(150, 300, 10, 5, "green")

# Crear vistas
square_view = ShapeView(window, square_model)
square2_view = ShapeView(window, square2_model)
square3_view = ShapeView(window, square3_model)

# Crear controladores
ShapeController(square_view, square_model)
ShapeController(square2_view, square2_model)
ShapeController(square3_view, square3_model)

window.mainloop()