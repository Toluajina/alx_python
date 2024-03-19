"""Rectangle class Module"""
BaseGeometry = __import__("5-base_geometry").BaseGeometry

class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Method Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validating value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class, inherits from Rectangle"""
    def __init__(self, size):
        """Initialize square method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Call parent class constructor with size as both width and height

    def area(self):
        """Method that returns area of square"""
        return self.__size ** 2
