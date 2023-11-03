import numpy as np

import art
from utils import log

RADIUS = 50
N = 15  # Number of nails around the circumference
IMAGE_PATH = "/Users/neshpatel/Downloads/plus.png"
SIZE = RADIUS * 2


def linear_algebra_lession():
    # art.plot_all_lines(NUM_NAILS, RADIUS)
    x = np.array([-1.3, -0.9, -0.3, 0.3, 0.7, 1.3])
    y = np.array([-0.4, 0.4, 0.6, 1.5, 2.0, 2.1])

    A = np.array([np.ones(len(x)), x])
    A = np.column_stack([np.ones(len(x)), x])
    log.info(A.shape)
    log.info(y.shape)
    log.info(np.linalg.pinv(A).shape)
    X = np.linalg.pinv(A) @ y
    log.info(X)


def create_art():
    art.plot_all_lines(N, RADIUS)
    image = art.load_and_process_image(IMAGE_PATH)
    image.show()
    b = art.to_matrix(image).flatten()

    circle_points = art.get_circle_points(N, RADIUS)
    all_lines = art.get_all_line_points(circle_points)

    line_matrices = [art.plot_points(SIZE, l) for l in all_lines]
    A = np.array([l.flatten() for l in line_matrices]).T
    x = np.linalg.pinv(A) @ b
    
    keep_lines = np.array(x > 0.5)

    matrix = art.plot_points(SIZE, circle_points)
    for i, should_keep in enumerate(keep_lines):
        if should_keep:
            matrix = art.overlay_points(matrix, all_lines[i])

    art.to_image(matrix).show()


def main():
    pass


if __name__ == '__main__':
    main()