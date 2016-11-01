# vecttor python

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '>'

    def __add__(self, other):
        return Vector(other.x + self.x, other.y+self.y, other.z+self.y)