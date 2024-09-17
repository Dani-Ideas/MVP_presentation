from Controllers.mainController import mainController
import customtkinter as ctk

if __name__ == "__main__":
    root = ctk.CTk()  
    app = mainController(root)
    root.mainloop()
