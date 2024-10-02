from tkinter import *
def drag_pos(event):
    Object=event.widget
    Object.startX=event.x
    Object.startY=event.y
def drag(event):
    Object=event.widget
    x=Object.winfo_x() - Object.startX+event.x
    y=Object.winfo_y() - Object.startY+event.y
    Object.place(x=x,y=y)
window =Tk()
window.geometry("720x520")
square = Label(window,bg="blue",width=10,height=5)
square.place(x=0,y=0)
square2 = Label(window,bg="red",width=10,height=5)
square2.place(x=100,y=100)
square3 = Label(window,bg="green",width=10,height=5)
square3.place(x=150,y=300)
square2.bind("<Button-1>",drag_pos)
square2.bind("<B1-Motion>",drag)
square.bind("<Button-1>",drag_pos)
square.bind("<B1-Motion>",drag)
square3.bind("<Button-1>",drag_pos)
square3.bind("<B1-Motion>",drag)
window.mainloop()