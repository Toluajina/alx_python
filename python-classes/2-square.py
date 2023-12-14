class Square:
    """
    A class that defines a square.

    Attributes:
    - __size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int, optional): The size of the square. Defaults to 0.
        """
        # Validate that size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Validate that size is non-negative
        if size < 0:
            raise ValueError("size must be >= 0")

        # Private instance attribute
        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

# Example usage:
try:
    mysquare = Square(5)
    print(mysquare.area())
except Exception as e:
    print(e)
