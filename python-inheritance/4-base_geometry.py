class BaseGeometry:
    """
    Represents base geometry.

    Public instance method:
        - area(self): Raises an Exception with the message "area() is not implemented."
    """

    def area(self):
        """Public instance method to raise an Exception."""
        raise Exception("area() is not implemented")