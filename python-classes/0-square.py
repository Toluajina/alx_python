class Square(object):
    def __init__(self, size):
        """
        Initializes a new instance of the Square class with the given size.

        Parameters:
            size: The size of the square.
        """
        self.__size = size

# Example usage:
# Instantiate a square with size 3
my_square = Square(3)

# Print the type and dictionary representation of the square
print(type(my_square))
print(my_square.__dict__)

# Instantiate another square with size 89 (using a different variable)
another_square = Square(89)

# Print the type and dictionary representation of the second square
print(type(another_square))
print(another_square.__dict__)
