import art

N = 300  # Number of nails around the circumference
IMAGE_PATH = ""
NUM_LINES = 2000  # Number of lines to draw


def main():
    art.gen_string_art(IMAGE_PATH, N, NUM_LINES)


if __name__ == '__main__':
    main()