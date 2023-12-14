class Square:
    def __init__(self, size):
        self.__size = size

# Example usage:
# Instantiate a square with size 3
my_square = Square(3)

# Print the type and dictionary representation of the square
print(type(my_square))
print(my_square.__dict__)