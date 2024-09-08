import customtkinter as ctk
import tkinter as tk
import os
from PIL import Image

class mainView:
    def __init__(self, root, controller):
        self.root = root  
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("blue") 
        # Título de la ventana
        self.root.title("Corporativo Alavez")
        self.root.geometry("800x550")

        # Cargar una imagen usando una ruta relativa
        self.image = Image.open(os.path.join(os.path.dirname(__file__), "..", "assets", "6089dddf2058ac387e4d37e2.png"))
        self.ctk_image = ctk.CTkImage(self.image, size=(250, 250))  # Usar CTkImage en lugar de PhotoImage

        # Colocar la imagen en la ventana
        self.image_label = ctk.CTkLabel(self.root, image=self.ctk_image, text="")
        self.image_label.pack(side=ctk.LEFT, pady=10)

        # Crear un frame
        frame = ctk.CTkFrame(master=self.root)
        frame.pack(side=tk.RIGHT, pady=20, padx=40, fill='y', expand=False)

        # Configurar el label dentro del frame
        label = ctk.CTkLabel(master=frame, text='Verificacion de usuario')
        label.pack(pady=12, padx=10)

        # Crear la caja de texto para el nombre de usuario
        self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Nombre de usuario")
        self.user_entry.pack(pady=12, padx=10)

        # Crear la caja de texto para la contraseña
        self.user_pass = ctk.CTkEntry(master=frame, placeholder_text="Contraseña", show="*")
        self.user_pass.pack(pady=12, padx=10)

        # Crear el botón de login
        button = ctk.CTkButton(master=frame, text='Login', corner_radius=32)
        button.pack(pady=12, padx=10)

    def update_image_label(self, img):
        # Redimensionar la imagen al tamaño deseado
        resized_image = img.resize((250, 250), Image.Resampling.LANCZOS)
        # Convertir la imagen redimensionada a CTkImage
        self.ctk_image = ctk.CTkImage(resized_image, size=(250, 250))
        # Actualizar la imagen en el widget
        self.image_label.configure(image=self.ctk_image)
