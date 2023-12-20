class Square(object):
    def __init__(self, size):
        """
        Initializes a new instance of the Square class with the given size.

        Parameters:
            size: The size of the square.
        """
        self.__size = size

my_square = Square(3)

print(type(my_square))
print(my_square.__dict__)

