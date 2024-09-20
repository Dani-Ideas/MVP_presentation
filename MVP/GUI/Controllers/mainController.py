from Models.mainModel import mainModel
from Views.log_in_View import log_in_View
from Controllers.panelControl_controller import panelControl_controller

class mainController:
    active = True

    def __init__(self, root):
        self.root = root
        # Inicializar el modelo y la vista
        self.model = mainModel()
        self.view = log_in_View(root, self)
        
        # Configuración específica de la animación de brillo
        self.root.bind('<Motion>', self.on_mouse_move)
        self.update_image_label(self.model.image1)

    def on_mouse_move(self, event):
        if mainController.active:
            x, y = event.x, event.y
            if x < self.root.winfo_width() // 2 and not self.model.animating:
                self.model.start_brightness_animation(self.model.image1, self.model.image2)
            elif x >= self.root.winfo_width() // 2 and not self.model.animating:
                self.model.start_brightness_animation(self.model.image2, self.model.image1)
            self.animate_brightness()

    def update_image_label(self, img):
        if img and mainController.active:  # Verifica que la imagen no sea None
            self.view.update_image_label(img)

    def animate_brightness(self):
        if self.model.animating and mainController.active:
            brightened_image = self.model.animate_brightness()
            if brightened_image:
                self.update_image_label(brightened_image)
                self.root.after(1200000, self.animate_brightness)
    
    def log_in(self):
        mainController.active = False
        self.view.destroy_view()
        panelControl_controller(self.root)
