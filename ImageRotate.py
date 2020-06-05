import os
from PIL import Image


def ImageRotate(Dirctry):
    Index = 1
    for f in os.listdir(f'{Dirctry}'):
        # fl, ex = os.path.splitext(f)
        im = Image.open(f'{Dirctry}/{f}')
        im.rotate(90).save(f'ImgRot{Index}.jpg')
        print(f'Processing Image: {f}')
        Index += 1


ImageResize(
    './Temp/')
