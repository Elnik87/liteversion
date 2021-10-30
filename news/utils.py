import os
import secrets

from PIL.Image import Image
from flask import current_app


def save_picture_news(form_picture):
    random_hex = secrets.token_hex(16)
    f_ext = form_picture.filename.split(".")[-1]
    picture_fn = random_hex + "." + f_ext
    print(picture_fn)
    full_path = os.path.join(current_app.root_path, "static", "newspicture")
    if not os.path.exists(full_path):
        os.mkdir(full_path)

    picture_path = os.path.join(full_path, picture_fn)
    output_size = (500, 500)
    form_picture.save(picture_path)
    return picture_fn
