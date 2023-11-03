import art
from utils import log

RADIUS = 100
NUM_NAILS = 10  # Number of nails around the circumference
IMAGE_PATH = "/Users/neshpatel/Downloads/image.png"

def main():
    art.plot_all_lines(NUM_NAILS, RADIUS)

    

if __name__ == '__main__':
    main()