class Square(object):
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with the given size.

        Parameters:
            size: The size of the square.
        """
        self.__size = size

# Example usage:
# Instantiate a square with size 3
mysquare = Square()

# Print the type and dictionary representation of the square
print(mysquare.__dict__)

