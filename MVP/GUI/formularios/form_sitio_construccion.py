import tkinter as tk
import customtkinter as ctk
from config import COLOR_CUERPO_PRINCIPAL

class FormularioSitioConstruccionDesign:

    def __init__(self, panel_principal, logo):
        # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.barra_inferior = tk.Frame(panel_principal)
        self.barra_inferior.pack(side=tk.BOTTOM, fill='both', expand=True)

        # Primer Label con texto
        self.labelTitulo = ctk.CTkLabel(
            self.barra_superior, text="Página en construcción", fg_color=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.configure(fg_color="#222d33", font=("Roboto", 30))
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        # Segundo Label con la imagen
        self.label_imagen = ctk.CTkLabel(self.barra_inferior, image=logo)
        self.label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        self.label_imagen.configure(fg_color="#fff", font=("Roboto", 10), bg_color=COLOR_CUERPO_PRINCIPAL)
