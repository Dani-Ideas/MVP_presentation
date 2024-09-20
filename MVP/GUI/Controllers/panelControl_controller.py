from Models.Emplyee import EmployeeModel
import tkinter as tk
from Views.panel_control_View import panel_control_View
from formularios.form_graficas_design import FormularioGraficasDesign
from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign

class panelControl_controller:
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
        FormularioGraficasDesign(self.view.cuerpo_principal)

    def abrir_panel_en_construccion(self):
        self.limpiar_panel(self.view.cuerpo_principal)
        FormularioSitioConstruccionDesign(self.view.cuerpo_principal, self.view.img_sitio_construccion)

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
