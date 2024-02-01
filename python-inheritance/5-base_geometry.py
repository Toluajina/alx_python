"""Defines a base geometry class BaseGeometry."""
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        # Validate if value is an integer
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        # Validate if value is greater than 0
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
