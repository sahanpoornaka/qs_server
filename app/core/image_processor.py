from fastapi import UploadFile

import PIL.Image as Image

from app.db.drive.images import get_drive


def get_image_dims(image_file: UploadFile):
    img = Image.open(image_file.file)
    width, height = img.size
    return width, height


def upload_image(image_name: str, image_file: UploadFile):
    drive = get_drive()
    width, height = get_image_dims(image_file)

    fp = image_file.file
    fp.seek(0)
    image_name = drive.put(name=image_name, data=fp, content_type="image/png")
    fp.close()

    return {"img_name": image_name, "img_dims": {"width": width, "height": height}}
