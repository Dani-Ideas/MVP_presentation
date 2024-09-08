from PIL import Image, ImageEnhance
import customtkinter as ctk

class ImageModel:
    def __init__(self):
        self.image1 = Image.open("/home/dani-ideas/Pictures/icons/6089dac8c78be84881ef4700.png").convert("RGBA")
        self.image2 = Image.open("/home/dani-ideas/Pictures/icons/6089db4cc78be84881ef4701.png").convert("RGBA")
        self.brightness_factor = 1.0
        self.fade_in = True
        self.animating = False
        self.image_from = self.image1
        self.image_to = self.image2

    def start_brightness_animation(self, img_from, img_to):
        self.animating = True
        self.brightness_factor = 1.0
        self.image_from = img_from
        self.image_to = img_to

    def animate_brightness(self):
        if self.fade_in:
            self.brightness_factor -= 0.05
        else:
            self.brightness_factor += 0.05

        if self.brightness_factor <= 0.0:
            self.brightness_factor = 0.0
            self.fade_in = False
            self.image_from = self.image_to

        if self.brightness_factor >= 1.0:
            self.brightness_factor = 1.0
            self.fade_in = True
            self.animating = False
            return

        enhancer = ImageEnhance.Brightness(self.image_from)
        brightened_image = enhancer.enhance(self.brightness_factor)
        return brightened_image
