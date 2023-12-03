import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0) 
 
# based on https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil

class HelloWorld:

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {
                    "image_width": ("INT", {"default": 512, "min": 64, "max": 2048}),
                    "image_height": ("INT", {"default": 512, "min": 64, "max": 2048}),        
                    "text": ("STRING", {"multiline": True, "default": "Hello World"}),
                    "font_size": ("INT", {"default": 50, "min": 1, "max": 1024}),
                    "font_color": (["white", "black", "red", "green", "blue", "yellow"],),
                    "background_color": (["white", "black", "red", "green", "blue", "yellow"],),
                    }
                }

    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("IMAGE",)
    FUNCTION = "write_text"
    CATEGORY = "Tutorial Nodes"

    def write_text(self, image_width, image_height, text, 
                   font_size, font_color, background_color):

        # Create a new PIL image
        new_img = Image.new("RGBA", (image_width, image_height), background_color) 
        draw = ImageDraw.Draw(new_img)

        # Define font
        font = ImageFont.truetype("arial.ttf", size=font_size) 
        
        # Get the image center
        image_center_x = image_width/2
        image_center_y = image_height/2
        
        # Draw the text, mm = text center
        draw.text((image_center_x, image_center_y), text, fill=font_color, font=font, anchor="mm")
        
        # Convert the PIL image to a torch tensor
        image_out = pil2tensor(new_img),
        
        return (image_out)
 