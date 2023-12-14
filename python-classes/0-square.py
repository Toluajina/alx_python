class Square:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2


# Example usage:
# Instantiate a square with size 5
my_square = Square(5)

# Get the size of the square
print("Size of the square:", my_square.get_size())

# Set a new size for the square
my_square.set_size(7)
print("New size of the square:", my_square.get_size())

# Calculate and print the area of the square
print("Area of the square:", my_square.area())