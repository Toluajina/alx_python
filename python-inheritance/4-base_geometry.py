# 4-base_geometry.py
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

# Example usage:
try:
    geometry = BaseGeometry()
    geometry.area()
except Exception as e:
    print(e)