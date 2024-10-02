class ShapeController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.bind("<Button-1>", self.drag_start)
        self.view.bind("<B1-Motion>", self.drag)

    def drag_start(self, event):
        self.view.startX = event.x
        self.view.startY = event.y

    def drag(self, event):
        new_x = self.view.winfo_x() - self.view.startX + event.x
        new_y = self.view.winfo_y() - self.view.startY + event.y
        self.view.place(x=new_x, y=new_y)
