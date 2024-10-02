import os
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_imagenes as util_img
import util.util_ventana as util_ventana

class panel_control_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        
        # Carga de imágenes
        self.logo = util_img.leer_imagen_custom(os.path.join(os.path.dirname(__file__), '..', 'images', 'logo.png'), (560, 136))
        self.perfil = util_img.leer_imagen_custom(os.path.join(os.path.dirname(__file__), '..', 'images', 'photo_avatar_circle.png'), (100, 100))
        self.img_sitio_construccion = util_img.leer_imagen_custom(os.path.join(os.path.dirname(__file__), '..', 'images', 'sitio_construccion.png'), (200, 200))

        # Configuración de la ventana
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()


    def config_window(self):
        self.root.title('Corporación Alavez')
        icon_image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'logo.png')
        self.root.iconphoto(True, tk.PhotoImage(file=icon_image_path))  # Mantén PhotoImage para el icono de ventana

        w, h = 1024, 600
        util_ventana.centrar_ventana(self.root, w, h)

    def paneles(self):
        # Paneles principales con CustomTkinter
        self.barra_superior = ctk.CTkFrame(self.root, fg_color=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=ctk.TOP, fill='both')

        self.menu_lateral = ctk.CTkFrame(self.root, fg_color=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=ctk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = ctk.CTkFrame(self.root, fg_color=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=ctk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        # Barra superior
        font_awesome = ctk.CTkFont(family='FontAwesome', size=16)
        roboto_font_15 = ctk.CTkFont(family='Roboto', size=15)
        roboto_font_10 = ctk.CTkFont(family='Roboto', size=10)
    
        # Botón del menú lateral
        self.buttonMenuLateral = ctk.CTkButton(self.barra_superior, text="☰", font=font_awesome,
                                               command=self.controller.toggle_panel, fg_color=COLOR_BARRA_SUPERIOR, text_color="white")
        self.buttonMenuLateral.pack(side=ctk.LEFT)
    
        # Título
        self.labelTitulo = ctk.CTkLabel(self.barra_superior, text="Corporativo Alavez", text_color="white", font=roboto_font_15, fg_color=COLOR_BARRA_SUPERIOR)
        self.labelTitulo.pack(side=ctk.LEFT)
    
        # Nombre del empleado
        self.labelEmpleado = ctk.CTkLabel(self.barra_superior, text="Angel Alavez", text_color="white", font=roboto_font_10, fg_color=COLOR_BARRA_SUPERIOR)
        self.labelEmpleado.pack(side=ctk.RIGHT, pady=10)

    def controles_menu_lateral(self):
        # Configuración del menú lateral
        font_awesome = ctk.CTkFont(family='FontAwesome', size=15)

        # Etiqueta de perfil
        self.labelPerfil = ctk.CTkLabel(self.menu_lateral, text="", image=self.perfil, fg_color=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=ctk.TOP, pady=10)

        # Botones del menú lateral
        self.buttonDashBoard = ctk.CTkButton(self.menu_lateral, text="  \uf109    Productivity", font=font_awesome,
                                             fg_color=COLOR_MENU_LATERAL, text_color="white", width=200, height=40, command=self.controller.abrir_panel_graficas)
        self.buttonDashBoard.pack(side=ctk.TOP)

        self.buttonSettings = ctk.CTkButton(self.menu_lateral, text="  \uf013    Schedule", font=font_awesome,
                                            fg_color=COLOR_MENU_LATERAL, text_color="white", width=200, height=40, command=self.controller.abrir_panel_horario)
        self.buttonSettings.pack(side=ctk.TOP)

        self.buttonSettings = ctk.CTkButton(self.menu_lateral, text="  \uf013    Settings", font=font_awesome,
                                            fg_color=COLOR_MENU_LATERAL, text_color="white", width=200, height=40, command=self.controller.abrir_panel_en_construccion)
        self.buttonSettings.pack(side=ctk.TOP)

    def controles_cuerpo(self):
        # Imagen principal
        label = ctk.CTkLabel(self.cuerpo_principal, image=self.logo, fg_color=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)
