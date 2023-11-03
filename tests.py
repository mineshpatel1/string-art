import unittest
import numpy as np

import art

RADIUS = 100
SIZE = RADIUS * 2
N = 10

class TestGeometry(unittest.TestCase):

    def test_circle_points(self):
        expected = [
            np.array([199, 100]),
            np.array([180, 158]),
            np.array([130, 195]),
            np.array([69, 195]),
            np.array([19, 158]),
            np.array([0, 100]),
            np.array([19, 41]),
            np.array([69, 4]),
            np.array([130, 4]),
            np.array([180, 41]),
        ]

        points = art.get_circle_points(N, RADIUS)
        for i, p in enumerate(points):
            self.assertTrue(np.array_equal(p, expected[i]))

    def test_line_points(self):
        expected_line = np.array([
            [130, 195],
            [129, 194],
            [128, 192],
            [127, 191],
            [126, 189],
            [125, 188],
            [124, 187],
            [123, 185],
            [122, 184],
            [121, 182],
            [120, 181],
            [119, 180],
            [118, 178],
            [117, 177],
            [116, 175],
            [115, 174],
            [114, 173],
            [113, 171],
            [112, 170],
            [111, 168],
            [110, 167],
            [109, 166],
            [108, 164],
            [107, 163],
            [106, 161],
            [105, 160],
            [104, 159],
            [103, 157],
            [102, 156],
            [101, 154],
            [100, 153],
            [99, 152],
            [98, 150],
            [97, 149],
            [96, 147],
            [95, 146],
            [94, 145],
            [93, 143],
            [92, 142],
            [91, 140],
            [90, 139],
            [89, 138],
            [88, 136],
            [87, 135],
            [86, 133],
            [85, 132],
            [84, 131],
            [83, 129],
            [82, 128],
            [81, 126],
            [80, 125],
            [79, 124],
            [78, 122],
            [77, 121],
            [76, 119],
            [74, 118],
            [73, 117],
            [72, 115],
            [71, 114],
            [70, 112],
            [69, 111],
            [68, 110],
            [67, 108],
            [66, 107],
            [65, 105],
            [64, 104],
            [63, 103],
            [62, 101],
            [61, 100],
            [60, 98],
            [59, 97],
            [58, 96],
            [57, 94],
            [56, 93],
            [55, 91],
            [54, 90],
            [53, 89],
            [52, 87],
            [51, 86],
            [50, 84],
            [49, 83],
            [48, 82],
            [47, 80],
            [46, 79],
            [45, 77],
            [44, 76],
            [43, 75],
            [42, 73],
            [41, 72],
            [40, 70],
            [39, 69],
            [38, 68],
            [37, 66],
            [36, 65],
            [35, 63],
            [34, 62],
            [33, 61],
            [32, 59],
            [31, 58],
            [30, 56],
            [29, 55],
            [28, 54],
            [27, 52],
            [26, 51],
            [25, 49],
            [24, 48],
            [23, 47],
            [22, 45],
            [21, 44],
            [20, 42],
            [19, 41],
        ])

        points = art.get_circle_points(N, RADIUS)
        line_points = art.get_all_line_points(points)
        expected = int((N * (N - 1)) / 2)

        self.assertEqual(len(line_points), 45)
        self.assertEqual(len(line_points), expected)
        self.assertTrue(np.array_equal(line_points[20], expected_line))

if __name__ == '__main__':
    unittest.main()