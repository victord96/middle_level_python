class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, another_coordinate):
        x_diff = (self.x - another_coordinate.x)**2
        y_diff = (self.y - another_coordinate.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordinate(3, 30)
    coord_2 = Coordinate(4, 8)

    print(coord_1.distance(coord_2))
    print(isinstance(3, Coordinate))