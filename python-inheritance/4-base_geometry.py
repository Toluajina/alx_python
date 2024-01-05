class MetaClass(type):
    """
    Metaclass to override dir() method and exclude __init_subclass__
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass=MetaClass):
    """
    BaseGeometry class that uses the overridden dir() method
    """
    def __dir__(self):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """Not implemented."""
        raise NotImplementedError("area() is not implemented")