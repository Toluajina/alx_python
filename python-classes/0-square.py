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

# Attempting to access the size directly will result in an AttributeError
# print(my_square.__size)  # This line will raise an AttributeError

# Access the size using a getter method (optional)
def get_size(self):
    return self.__size

