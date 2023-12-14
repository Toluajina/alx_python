class Square:
    def __init__(self, size):
        self.__size = size

    def get_size(self):  # Move the get_size method inside the class
        return self.__size

# Example usage:
# Instantiate a square with size 3
my_square = Square(3)

# Print the type and dictionary representation of the square
print(type(my_square))
print(my_square.__dict__)