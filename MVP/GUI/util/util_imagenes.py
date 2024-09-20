from PIL import ImageTk, Image
import customtkinter as ctk
import os

def leer_imagen(path, size):
    try:
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))
    except Exception as e:
        print(f"Error al cargar la imagen '{path}': {e}. Cargando imagen de respaldo.")
        try:
            path_respaldo = os.path.join(os.path.dirname(__file__), 'image', 'photo.png')
            return ImageTk.PhotoImage(Image.open(path_respaldo).resize(size, Image.ADAPTIVE))
        except Exception as e_respaldo:
            print(f"Error al cargar la imagen de respaldo: {e_respaldo}")
            return None  

def leer_imagen_custom(path, size):
    try:
        image = Image.open(path)
        image = image.resize(size, Image.LANCZOS)  
        return ctk.CTkImage(light_image=image, dark_image=image,size=size)
    except Exception as e:
        print(f"Error al cargar la imagen personalizada '{path}': {e}. Cargando imagen de respaldo.")
        try:
            path_respaldo = os.path.join(os.path.dirname(__file__), 'image', 'photo.png')
            image_respaldo = Image.open(path_respaldo).resize(size, Image.LANCZOS)
            return ctk.CTkImage(light_image=image_respaldo, dark_image=image_respaldo,size=size)
        except Exception as e_respaldo:
            print(f"Error al cargar la imagen de respaldo: {e_respaldo}")
            return None  
