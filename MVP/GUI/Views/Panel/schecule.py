import tkinter as tk
import customtkinter as ctk
from config import COLOR_CUERPO_PRINCIPAL
from Models.EmplyeeModel import EmployeeModel
from Models.ProcessModel import ProcessModel

class Shecule():
    def __init__(self, panel_principal):    
        #shecule_frame = ctk.CTkFrame(panel_principal, width=720, height=520)
        #shecule_frame.pack(fill="both", expand=True)

        self.labelTitulo = ctk.CTkLabel(
            panel_principal, text="Página en construcción", fg_color=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.configure(fg_color="#222d33", font=("Roboto", 30))
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)