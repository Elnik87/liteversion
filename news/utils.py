import os
import secrets

from PIL.Image import Image
from flask import current_app


def save_picture_news(form_picture):
    random_hex = secrets.token_hex(16)
    _, f_ext = os.path.splittext(form_picture.filename)
    picture_fn = random_hex + f_ext
    full_path = os.path.join(current_app.root_path, "static", "newspicture")
    if not os.path.exists(full_path):
        os.mkdir(full_path)

    picture_path = os.path.join(full_path, picture_fn)
    output_size = (500, 500)

    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)
    return picture_fn
