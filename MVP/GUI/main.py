from Controllers.mainController import mainController
import customtkinter as ctk

if __name__ == "__main__":
    root = ctk.CTk()  # Usar CTk en lugar de Tk
    root.title("Login")
    app = mainController(root)
    root.mainloop()
