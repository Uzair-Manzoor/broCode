# super() = Function used to give access to the method of parant class.
#           Returns a temporary object of a parant class when used

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square (Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height) :
        super(Cube, self).__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())
