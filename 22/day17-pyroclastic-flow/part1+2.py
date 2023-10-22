#!python3

with open('input.txt') as file:
    input_str = file.read()

def Shape:
    def __init__(self, width: int, occupied: set, right_contour: set, left_contour: set, bottom_contour: set):
        self.width = width
        self.occupied = occupied
        self.right_contour = right_contour
        self.left_contour = left_contour
        self.bottom_contour = bottom_contour

shapes = [
    Shape(
        width=4,
        occupied={(0, 0), (1, 0), (2, 0), (3, 0)},
        right_contour={(4, 0)},
        left_contour={(-1, 0)},
        occupied={(0, -1), (1, -1), (2, -1), (3, -1)}
    ),
    Shape(
        width=3,
        occupied={(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
        right_contour={(4, 0)},
        left_contour={(-1, 0)},
        occupied={(0, -1), (1, -1), (2, -1), (3, -1)}
    )
]
