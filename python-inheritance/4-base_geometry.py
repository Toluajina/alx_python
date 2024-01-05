class MetaClass(type):
    """
    Metaclass to override dir() method and exclude __init_subclass__
    """
    def __dir__(cls):
        """
        Override dir() method to exclude __init_subclass__.

        Returns:
        - list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass=MetaClass):
    """
    BaseGeometry class that uses the overridden dir() method
    """
    def __dir__(self):
        """
        Override dir() method to exclude __init_subclass__.

        Returns:
        - list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """
        Not implemented.

        Raises:
        - NotImplementedError: With the message "area() is not implemented."
        """
        raise NotImplementedError("area() is not implemented")
