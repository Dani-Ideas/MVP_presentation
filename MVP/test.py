import customtkinter as ctk
from PIL import Image, ImageTk, ImageEnhance

class MouseImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transición de brillo en CustomTkinter")
        self.root.geometry("800x600")

        # Obtener el modo de apariencia (oscuro o claro)
        self.appearance_mode = ctk.get_appearance_mode()

        # Fondo según el tema del sistema
        if self.appearance_mode == "Dark":
            self.transition_color = (0, 0, 0)  # Negro
        else:
            self.transition_color = (255, 255, 255)  # Blanco

        # Cargar las imágenes originales y convertirlas a modo RGBA para transparencia
        self.image1 = Image.open("/home/dani-ideas/Pictures/icons/6089dac8c78be84881ef4700.png").convert("RGBA")
        self.image2 = Image.open("/home/dani-ideas/Pictures/icons/6089db4cc78be84881ef4701.png").convert("RGBA")

        # Mostrar la primera imagen escalada
        self.update_image_label(self.image1)

        # Inicializar variables de control para la animación de brillo
        self.brightness_factor = 1.0
        self.fade_in = True
        self.animating = False

        # Detectar movimiento del mouse
        self.root.bind('<Motion>', self.on_mouse_move)

    def on_mouse_move(self, event):
        x, y = event.x, event.y

        # Iniciar la animación si el mouse cruza la mitad de la pantalla
        if x < self.root.winfo_width() // 2 and not self.animating:
            self.start_brightness_animation(self.image1, self.image2)
        elif x >= self.root.winfo_width() // 2 and not self.animating:
            self.start_brightness_animation(self.image2, self.image1)

    def update_image_label(self, img):
        # Redimensionar la imagen al tamaño del widget
        scaled_image = img.resize((self.root.winfo_width(), self.root.winfo_height()), Image.Resampling.LANCZOS)
        self.displayed_image = ImageTk.PhotoImage(scaled_image)
        self.image_label = ctk.CTkLabel(self.root, image=self.displayed_image)
        self.image_label.pack(pady=20)

    def start_brightness_animation(self, img_from, img_to):
        self.animating = True
        self.brightness_factor = 1.0  # Reseteamos el brillo para la animación
        self.image_from = img_from
        self.image_to = img_to
        self.animate_brightness()

    def animate_brightness(self):
        # Reducir el brillo de la imagen actual
        if self.fade_in:
            self.brightness_factor -= 0.05
        else:
            self.brightness_factor += 0.05

        # Si el brillo llega a 0, cambiar a la nueva imagen
        if self.brightness_factor <= 0.0:
            self.brightness_factor = 0.0
            self.fade_in = False  # Comenzar a aumentar el brillo de la nueva imagen
            self.image_from = self.image_to

        # Si el brillo llega a 1, detener la animación
        if self.brightness_factor >= 1.0:
            self.brightness_factor = 1.0
            self.fade_in = True  # Preparar para la próxima animación
            self.animating = False
            return

        # Ajustar el brillo de la imagen actual
        enhancer = ImageEnhance.Brightness(self.image_from)
        brightened_image = enhancer.enhance(self.brightness_factor)

        # Escalar la imagen con el brillo ajustado
        brightened_image = brightened_image.resize((self.root.winfo_width(), self.root.winfo_height()), Image.Resampling.LANCZOS)
        self.displayed_image = ImageTk.PhotoImage(brightened_image)

        # Actualizar la imagen mostrada
        self.image_label.configure(image=self.displayed_image)

        # Continuar la animación
        self.root.after(50, self.animate_brightness)  # Ajusta la velocidad de la animación

if __name__ == "__main__":
    ctk.set_appearance_mode("system")  # Ajustar el modo según el sistema
    root = ctk.CTk()
    app = MouseImageApp(root)
    root.mainloop()
