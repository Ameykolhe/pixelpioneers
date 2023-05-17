import logging

import numpy as np
from PIL import Image, UnidentifiedImageError

from pixelpioneers.exceptions import ImageIOError
from pixelpioneers.image_io._abstract_io import AbstractImageReader, AbstractImageWriter

class BMPHandler(AbstractImageReader, AbstractImageWriter):
    def read(self, path: str) -> np.ndarray:
        try: 
            img = Image.open(path, formats=["bmp"])
            img_array = np.array(img)
            return img_array
        except FileNotFoundError as fnfe:
            raise ImageIOError(f"Error reading image: File '{path}' not found.")

        except UnidentifiedImageError as uie:
            raise ImageIOError(f"Error reading image: Unrecognized file format.")

        except Exception as e:
            raise ImageIOError
    
    def write(self, path: str, image: np.ndarray) -> bool:
        img = Image.fromarray(image)
        img.save(path)
        return True


if __name__ == "__main__":
    bmpHandler = BMPHandler()
    img = bmpHandler.read("data/sample.bmp")
    bmpHandler.write("data/sample_out.bmp", img)