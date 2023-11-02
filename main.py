from PIL import Image, ImageDraw
from utils import log
import numpy as np

RADIUS = 512
NUM_NAILS = 10  # Number of nails around the circumference
IMAGE_PATH = "/Users/neshpatel/Downloads/image.png"


def load_grayscale_image() -> np.array:
    image = Image.open(IMAGE_PATH)
    return image.convert("L")  # Convert to grayscale


def to_array(image: Image) -> np.array:
    image_array = np.array(image)
    image_array = image_array / 255  # Normalise
    return image_array


def to_image(array: np.array) -> Image:
    array *= 255
    return Image.fromarray(array)


def crop_image(image: Image) -> Image:
    image = image.convert("RGBA")
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)
    result = Image.composite(image, Image.new('RGBA', image.size, (0, 0, 0, 0)), mask)
    result = result.convert("L")
    return result


def get_circle_points(num_points: int, radius: int) -> np.ndarray:
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


def get_line_points(p0: tuple[int, int], p1: tuple[int, int]) -> np.ndarray:
    num_points = max(abs(p1[0] - p0[0]), abs(p1[1] - p0[0]))
    x = np.linspace(p0[0], p1[0], num_points)
    y = np.linspace(p0[1], p1[1], num_points)

    x = np.round(x).astype(int)
    y = np.round(y).astype(int)

    return np.column_stack((x, y))


def plot_points(size: int, points: np.ndarray) -> np.array:
    matrix = np.zeros((size, size), dtype=np.uint8)
    matrix[points[:, 1], points[:, 0]] = 1
    return matrix


def overlay_points(base: np.array, points: np.ndarray) -> np.array:
    base[points[:, 1], points[:, 0]] = 1
    return base


def plot_all_lines():
    """Simply quite pretty."""

    image = load_grayscale_image()
    radius = int(image.size[0] / 2)
    points = get_circle_points(NUM_NAILS, int(radius))
    matrix = plot_points(radius * 2, points)

    for p0 in points:
        for p1 in points:
            if not np.array_equal(p0, p1):
                line_points = get_line_points(p0, p1)
                matrix = overlay_points(matrix, line_points)

    image = to_image(matrix)
    image.show()


def main():
    plot_all_lines()
    

if __name__ == '__main__':
    main()