import math
import numpy as np
from PIL import Image, ImageDraw
from tqdm import tqdm
from typing import Optional

import art
from utils import log, np_in_array

RADIUS = 512
N = 250  # Number of nails around the circumference
IMAGE_PATH = "/Users/neshpatel/Downloads/original.png"
SIZE = RADIUS * 2
NUM_LINES = 100


def calc_error(matrix_1: np.array, matrix_2: np.array) -> float:
    return np.sum((matrix_1 - matrix_2) ** 2)


def find_best_line(
    target: np.array,
    current: np.array,
    p0: np.array,
    possible_points: list[np.array],
) -> tuple[np.array, float]:
    best_line = None
    lowest_error = calc_error(current, target)

    for p1 in possible_points:
        line = art.get_line_points(p0, p1)
        A = art.overlay_points(current.copy(), line)
        error = np.sum((target - A) ** 2)
        if error < lowest_error:
            lowest_error = error
            best_line = line
    return best_line, lowest_error


def main():
    image = art.load_and_process_image(IMAGE_PATH)
    I = art.to_matrix(image)  # Image Matrix

    pin_points = art.get_circle_points(N, RADIUS)
    canvas = art.plot_points(SIZE, pin_points)
    
    log.newline()
    log.info("Plotting all lines...")
    
    best_line = None

    for _ in tqdm(range(NUM_LINES)):
        if best_line is None:  # First run
            p0 = pin_points[0]  # Start arbitrarily, waste of compute finding the optimal
            used_pins = [p0]
        else:
            p0 = best_line[-1]
            used_pins = [best_line[0], p0]

        possible_points = [p for p in pin_points if not np_in_array(p, used_pins)]
        best_line, _ = find_best_line(I, canvas.copy(), p0, possible_points)
        if best_line is None:
            break
        art.overlay_points(canvas, best_line)

    art.to_image(canvas).show()

    
    



if __name__ == '__main__':
    main()