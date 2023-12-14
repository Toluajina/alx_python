class Square:
    """
    A class that defines a square.

    Attributes:
    - __size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size: The size of the square.
        """
        # Private instance attribute
        self.__size = size

# Example usage:

my_square = Square()
print(type(my_square))
print(my_square.__dict__)