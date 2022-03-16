import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def touches(self, other):
        return math.sqrt(math.pow((self.x - other.x), 2) + math.pow((self.y - other.y), 2)) == self.r + other.r


# Case 1
c1 = Circle(0, 0, 1)
c2 = Circle(5, 0, 1)
assert not c1.touches(c2)

# Case 2
c1 = Circle(0, 0, 1)
c2 = Circle(2, 0, 1)
assert c1.touches(c2)

# Case 3
c1 = Circle(0, 0, 1)
c2 = Circle(1, 0, 1)
assert not c1.touches(c2)

# Case 4
c1 = Circle(0, 0, 2)
c2 = Circle(1, 0, 1)
assert not c1.touches(c2)

# Case 5
c1 = Circle(0, 0, 2)
c2 = Circle(0.25, 0, 1)
assert not c1.touches(c2)
