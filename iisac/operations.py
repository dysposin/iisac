from itertools import zip_longest
import os

# system utilities



def clear_console():
    """
    Clears console for screen refresh
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# image operations

def expand(image: list, x: int=0, y: int=0, fill: str=' ') -> list:
    """
    Expands the image in positive direction with empty cells and rows
    """
    new_width = len(image[0]) + x
    return [row + [fill]*x for row in image] + [[fill]*new_width]*y


def translate(image: list, x: int=0, y: int=0) -> list:
    """
    Translates the image with wrap-around
    """
    return [row[-1*x:] + row[:-1*x] for row in (image[-1*y:] + image[:-1*y])]


def crop(image: list, x: int = 0, y: int = 0, width: int = 0, height:int = 0) -> list:
    """
    Crops the image, default is the size of the terminal
    """
    return [row[x:x+width] for row in image][y:y+height]


def equalize_sizes(image1: list, image2: list, fill: str) -> list:
    """
    Equalize two images to same size
    """
    size1 = size(image1)
    size2 = size(image2)
    final_size = tuple(max(i, j) for i, j in zip(size1, size2))

    if size1 < final_size:
        image1 = expand(image1, *size_delta(final_size, size1), fill=fill)
    if size2 < final_size:
        image2 = expand(image2, *size_delta(final_size, size2), fill=fill)
    return image1, image2



def add(image1: list, image2: list, fill, transparent: list) -> list:
    """
    Adds image2 on top of image1 excluding cells with transparency
    """
    image = []
    for row in list(zip_longest(image1, image2, fillvalue=[])):
        row = [c[1] if c[1] not in transparent
               else c[0]
                for c in list(zip_longest(row[0], row[1], fillvalue=' '))]
        image.append(row)
    return image


def draw(image: list, linebreak: str='', delimiter: str=''):
    """
    Draw image in terminal
    """
    for row in image:
        print(delimiter.join(row) + linebreak)


def merge(image1: list, image2: list, transparent: list) -> list:
    """
    Merges image1 and image2 cell-wise
    """
    image = []
    for row in list(zip_longest(image1, image2, fillvalue=[])):
        row = [c[1] + c[0] if c[1] not in transparent and c[0] is not None
               else c[1] if c[0] is None
               else c[0]
               for c in list(zip_longest(row[0], row[1]))]
        image.append(row)

    return image


# miscellaneous

def clamp(n: int, n_min: int, n_max: int) -> int:
    return max(n_min, min(n, n_min))


def size_delta(size1: tuple, size2: tuple) -> tuple:
    return (abs(size1[0] - size2[0]), abs(size1[1] - size2[1]))


def size(image: list) -> tuple:
    return (len(image[0]), len(image))
