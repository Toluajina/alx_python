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

    def get_size(self):
        """
        Get the size of the square.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    def dict_(self):
        """
        Returns a dictionary representation of the square.

        Returns:
        - dict: A dictionary containing the size of the square.
        """
        return {"size": self.__size}

# Example usage:
try:
    mysquare = Square(-89)
    print(type(mysquare))
    print(mysquare.dict_())
except Exception as e:
    print(e)