import numpy as np
from PIL import Image, ImageDraw, ImageOps
from utils import log
from itertools import combinations

WEIGHT = 0.2

def load_and_process_image(path: str) -> np.array:
    image = Image.open(path)
    image = image.convert("L")  # Convert to grayscale
    image = ImageOps.invert(image)
    return crop_image(image)


def to_matrix(image: Image) -> np.array:
    image_array = np.array(image)
    image_array = image_array / 255  # Normalise
    return image_array


def to_image(array: np.array) -> Image:
    array *= 255
    return Image.fromarray(array)


def crop_image(image: Image) -> Image:
    """Crops image to a circle."""
    image = image.convert("RGBA")
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
    result = Image.composite(image, Image.new('RGBA', image.size, (0, 0, 0, 0)), mask)
    result = result.convert("L")
    return result


def get_circle_points(num_points: int, radius: int) -> np.array:
    c_x, c_y = radius, radius

    x_array = []
    y_array = []
    for i in range(num_points):
        x = int(c_x + radius * np.cos(2 * np.pi * i / num_points))
        y = int(c_y + radius * np.sin(2 * np.pi * i / num_points))

        # Due to rounding, we can get points outside the bounds, just offset these by a pixel
        if x == radius * 2:
            x -= 1

        if y == radius * 2:
            y -= 1

        x_array.append(x)
        y_array.append(y)

    return np.column_stack((np.array(x_array), np.array(y_array)))


def get_line_points(p0: tuple[int, int], p1: tuple[int, int]) -> np.array:
    num_points = max(abs(p1[0] - p0[0]), abs(p1[1] - p0[0]))
    x = np.linspace(p0[0], p1[0], num_points)
    y = np.linspace(p0[1], p1[1], num_points)

    x = np.round(x).astype(int)
    y = np.round(y).astype(int)

    return np.column_stack((x, y))


def plot_points(
    size: int,
    points: np.array,
    weight: float = WEIGHT,
) -> np.array:
    matrix = np.zeros((size, size), dtype=np.float64)
    matrix[points[:, 1], points[:, 0]] = weight
    return matrix


def overlay_points(
    base: np.array,
    points: np.array,
    weight: float = WEIGHT,
) -> np.array:
    np.add.at(base, (points[:, 1], points[:, 0]), weight)
    np.clip(base, 0, 1, out=base)
    return base


def get_all_line_points(points: np.array) -> list[np.array]:
    all_lines = []
    for p0, p1 in combinations(points, 2):
        line_points = get_line_points(p0, p1)
        all_lines.append(line_points)
    return all_lines


def plot_all_lines(num_points: int, radius: int):
    log.info("Plotting all lines...")
    size = radius * 2
    circle_points = get_circle_points(num_points, radius)
    matrix = plot_points(size, circle_points)
    all_lines = get_all_line_points(circle_points)
    
    for line in all_lines:
        matrix = overlay_points(matrix, line)

    image = to_image(matrix)
    image.show()
