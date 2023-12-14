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
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
        - value (int): The new size of the square.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

# Example usage:
my_square = Square(5)
print(my_square.size)  # Accessing size using the property getter
print(my_square.area())  # Calculating and printing the area

# Setting a new size using the property setter
my_square.size = 3
print(my_square.size)
print(my_square.area())
