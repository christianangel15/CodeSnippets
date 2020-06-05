import os
from PIL import Image

size = 1200, 1200


def ImageResize(Dirctry):
    Index = 1
    for f in os.listdir(f'{Dirctry}'):
        # fl, ex = os.path.splitext(f)
        im = Image.open(f'{Dirctry}/{f}')
        im.thumbnail(size)
        im.save(f'ImgSiz{Index}.jpg')
        print(f'Processing Image: {f}')
        Index += 1


ImageResize(
    './Temp/')
