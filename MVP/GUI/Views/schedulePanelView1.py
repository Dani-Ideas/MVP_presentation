import os
import customtkinter as ctk
import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
from tkinter import font as tkfont

class schedulePanelView1:
    theme = ["#F2E8DF","#586E73","#0F3240","#011526","#010626","#2c3439"]
    
    def __init__(self, root, controller):
        self.root = root  
        self.controller = controller
        self.setup_ui()  

    def setup_ui(self):  # Definición correcta del método
        width = self.root.winfo_screenwidth() 
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        self.root.title("Control Panel")

        # Cabeza de ventana
        head_window_fm = ctk.CTkFrame(master=self.root, fg_color=schedulePanelView1.theme[3])
        head_window_fm.pack(fill="x", side="top")  
        
        self.toggle_btn = ctk.CTkButton(head_window_fm, text='☰', fg_color=schedulePanelView1.theme[4], text_color='white', font=('Bold', 25), corner_radius=0, hover_color=schedulePanelView1.theme[5], command=self.toogle_menu)
        self.toggle_btn.pack(side=ctk.LEFT)

        title_head = ctk.CTkLabel(head_window_fm, text='control panel', fg_color=schedulePanelView1.theme[4], text_color='white', font=('Bold', 16))
        title_head.pack(side=ctk.LEFT)

        # Crear el body
        self.body_window = ctk.CTkFrame(master=self.root, fg_color="red")
        self.body_window.pack(expand=True, fill=ctk.BOTH)
        #Crear el contenedor de la derecha
        self.content_window = ctk.CTkFrame(master=self.body_window, fg_color=schedulePanelView1.theme[1])
        self.content_window.pack(side=ctk.RIGHT, fill=ctk.BOTH,expand=True)
        # Crear el Covertor (Imagen original)
        image_path = os.path.join(os.path.dirname(__file__), "..", "assets", "jesus-eca-wewzzx11ShI-unsplash.jpg")
        self.original_image = Image.open(image_path)
        self.covertor_label = ctk.CTkLabel(self.content_window, text="", fg_color=schedulePanelView1.theme[0])# Crear un Label que contiene la imagen
        self.covertor_label.place(relwidth=1, relheight=0.15)# Usar place() para que mantenga proporciones relativas (relwidth, relheight)

        # Detectar cambios de tamaño en el label
        self.covertor_label.bind("<Configure>", self.resize_image)


    def toogle_menu(self):
        # Crear el menú desplegable dentro del body
        def toggle_menu_destroy():
                toggle_menu_fm.destroy()
                self.toggle_btn.configure(text='☰')
                self.toggle_btn.configure(command=self.toogle_menu)

        toggle_menu_fm = ctk.CTkFrame(master=self.body_window, fg_color=schedulePanelView1.theme[5])
        toggle_menu_fm.place(relwidth=0.1, relheight=1)
        self.toggle_btn.configure(text='<<')
        self.toggle_btn.configure(command=toggle_menu_destroy)
        # Crear la barra de menú usando tkinter.Menu
        #AGREGAR ESTO DESPUES DE TENER LISTO EL WINDOW CONTENT
        #AGREGAR ESTO DESPUES DE TENER LISTO EL WINDOW CONTENT
        #menubar = Menu(self.root) 
        #menu_font = tkfont.Font(size=24) 
#
        #file = Menu(menubar, tearoff=0) 
        #menubar.add_cascade(label='☰', menu=file, font=menu_font) 
        #file.add_command(label='New File', command=None) 
        #file.add_command(label='Open...', command=None) 
        #file.add_command(label='Save', command=None) 
        #file.add_separator() 
        #file.add_command(label='Exit', command=self.root.destroy)
        #AGREGAR ESTO DESPUES DE TENER LISTO EL WINDOW CONTENT
        #AGREGAR ESTO DESPUES DE TENER LISTO EL WINDOW CONTENT

    def resize_image(self, event):
        # Obtener el tamaño actual del label
        label_width = event.width
        label_height = event.height
        # Redimensionar la imagen para ajustarla al label
        resized_image = self.original_image.resize((label_width, label_height), Image.LANCZOS)

        # Convertir la imagen redimensionada a CTkImage y actualizar el Label
        self.covertor_image = ctk.CTkImage(resized_image)
        self.covertor_label.configure(image=self.covertor_image)
