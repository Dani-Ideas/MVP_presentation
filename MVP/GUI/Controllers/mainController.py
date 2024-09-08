import customtkinter as ctk
from Models.mainModel import mainModel
from Views.mainView import mainView

class mainController:
    def __init__(self, root):
        self.root = root
        # Inicializar el modelo y la vista
        self.model = mainModel()
        self.view = mainView(root, self)
        
        # Configuración específica de la animación de brillo
        self.root.bind('<Motion>', self.on_mouse_move)
        self.update_image_label(self.model.image1)

    def on_mouse_move(self, event):
        x, y = event.x, event.y
        if x < self.root.winfo_width() // 2 and not self.model.animating:
            self.model.start_brightness_animation(self.model.image1, self.model.image2)
        elif x >= self.root.winfo_width() // 2 and not self.model.animating:
            self.model.start_brightness_animation(self.model.image2, self.model.image1)
        self.animate_brightness()

    def update_image_label(self, img):
        if img:  # Verifica que la imagen no sea None
            self.view.update_image_label(img)

    def animate_brightness(self):
        if self.model.animating:
            brightened_image = self.model.animate_brightness()
            if brightened_image:
                self.update_image_label(brightened_image)
                self.root.after(1500, self.animate_brightness)

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Login")

    # Instanciar el controlador
    app = mainController(root)
    
    root.mainloop()
