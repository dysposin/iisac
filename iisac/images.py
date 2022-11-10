from math import sqrt

# generators

def generate_blank(width: int, height: int, fill: str) -> list:
    """
    Generates a width * height table filled with the fill character
    """
    return [[fill]*width]*height


def color_columns(width: int, height: int, colors: list, column_width: int = 8) -> list:
    """
    Generates colored columns
    """
    base = [None]*width
    for x in range(0, width):
        base[x] = colors[int((x / column_width) % len(colors))]
    image_colors = [base]*height

    return image_colors


def color_grid(width: int, height: int,  colors: list, grid_size: int = 8) -> list:
    """
    Generates a colored grid
    """
    width = ((width // grid_size)) * grid_size + grid_size
    base = [None]*width
    image_colors = []*height

    for y in range(0, height):
        for x in range(0, width):
            base[x] = colors[int((x / grid_size) % len(colors))]
        row_shift = int(y / grid_size)*grid_size
        image_colors.append(base[row_shift:] + base[:row_shift])
    return image_colors


def generate_coordinates(width: int, height: int) -> list:
    """
    Generates coordinates around the screen
    """
    c_horizontal = list('0123456789ABCDEF')
    coordinates = [[' ']*3 + c_horizontal[:width] + c_horizontal*(int(width/16))]

    for i in range(height):
        row = [f'{i:02}'] + [' ']*width
        coordinates.append(row)

    return coordinates


def ball(radius: int, palette: str=' .:-=+*#%@A') -> list:
    """
    Draws a ball
    """
    ball = [[sqrt((x-radius)**2 + (y-radius)**2) for x in range(radius*2)]
             for y in range(radius*2)]
    max_distance = max(max(ball))
    ball = [list(map(lambda x: palette[int(len(palette)/max_distance*int(x))], row))
            for row in ball]

    return ball


def box(width: int, height: int, style: str='light', fill: str=' ') -> list:
    """
    Draws a box
    """
    sides = {'light': (u'\u2500', u'\u2502'), # ─, │
             'heavy': (u'\u2501', u'\u2503')
    }
    corners = {'light': (u'\u250c', u'\u2510', u'\u2514', u'\u2518'), # ┌, ┐, └, ┘
               'heavy': (u'\u250f', u'\u2513', u'\u2517', u'\u251b')
    }
    single = u'\u2588'

    if height < 2:
        return width*single
    if width < 2:
        return [single]*height

    height -= 2
    width -= 2

    top = [[corners[style][0]] + [sides[style][0]]*width + [corners[style][1]]]
    bottom = [[corners[style][2]] + [sides[style][0]]*width + [corners[style][3]]]
    center = [[sides[style][1]] + [fill]*width + [sides[style][1]]]

    box = top + center*height + bottom

    return(box)

