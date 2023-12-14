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
try:
    mysquare = Square(5)
    print(mysquare.__size)  # Accessing __size directly (not recommended)
except Exception as e:
    print(e)
