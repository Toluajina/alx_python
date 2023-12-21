"""Defines a class Rectangle that inherits from BaseGeometry."""

class BaseGeometry:
    def area(self):
        """Placeholder for the area method."""
        raise NotImplementedError("area() method is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that the value is a positive integer.

        Parameters:
        - name (str): The name of the value being validated.
        - value (int): The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with given width and height.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

        Raises:
        - TypeError: If width or height is not an integer.
        - ValueError: If width or height is not a positive integer.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        - int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Format:
        [Rectangle] <width>/<height>

        Returns:
        - str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"