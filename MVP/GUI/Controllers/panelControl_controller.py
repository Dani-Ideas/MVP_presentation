from Models.EmplyeeModel import EmployeeModel
import tkinter as tk
from Views.panel_control_View import panel_control_View
from Views.Panel.graficas_mView import Graficas_mView
from Views.Panel.construccion_mView import Construccion_mView
from Views.Panel.schecule import Shecule

class panelControl_controller:
    #Agregar un cortafiuegos en caso de que la vista no se pudo cargar correctamente, implemetando una vita de: "algo salio mal" y una imagen 
    def __init__(self, root):
        self.root = root
        #self.user_model = EmployeeModel()
        self.view = panel_control_View(root, self)

    def toggle_panel(self):
        if self.view.menu_lateral.winfo_ismapped():
            self.view.menu_lateral.pack_forget()
        else:
            self.view.menu_lateral.pack(side=tk.LEFT, fill='y')

    def abrir_panel_graficas(self):
        self.limpiar_panel(self.view.cuerpo_principal)
        Graficas_mView(self.view.cuerpo_principal)
    
    def abrir_panel_horario(self):
        self.limpiar_panel(self.view.cuerpo_principal)
        Shecule(self.view.cuerpo_principal)

    def abrir_panel_en_construccion(self):
        self.limpiar_panel(self.view.cuerpo_principal)
        Construccion_mView(self.view.cuerpo_principal, self.view.img_sitio_construccion)

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
