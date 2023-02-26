import os
from PIL import Image
from flask import url_for, current_app
from base64 import b64encode
import base64

def add_profile_pic(pic_upload):
    image_pil = Image.open(pic_upload)
    print(f" pil image {type(image_pil)}")
    image_resize = image_pil.resize((500,500))
    print(f" image_resize {type(image_resize)}")
    image_bytes = image_resize.tobytes()
    print(f" image_bytes {type(image_bytes)}")
    #image_binary = base64.b64encode(image_bytes)
    #print(f" image_bnary {type(image_binary)}")
    return image_bytes


def decode_image(x):
    return b64encode(x).decode("utf-8")