class Square(object):
    def __init__(self, size):
        
        self.__size = size

my_square = Square(3)

def get_size(self):
    return self.__size

print(type(my_square))
print(my_square.__dict__)
