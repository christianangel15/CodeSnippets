from pdf2image import convert_from_bytes, convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError)
from PIL import Image
import PIL
import tempfile

Index = 1
with tempfile.TemporaryDirectory() as path:
    images = convert_from_bytes(open('YagniWedsAngel.pdf', 'rb').read())
    for image in images:
        img = f'Image{Index}.jpg'
        image.save(img)
        Index += 1
        print(f'Saving File {img}')
# --------------------------ANOTHER WAY-------------------------------
# images = convert_from_path('YagniWedsAngel.pdf', fmt='jpeg')
# Index = 1
# for image in images:
#     img = f'Image{Index}.jpg'
#     image.save(img)
#     Index += 1
#     print(f'Saving File {img}')
