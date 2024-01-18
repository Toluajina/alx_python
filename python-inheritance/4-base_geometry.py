# 4-base_geometry.py
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

# Testing the class
try:
    obj = BaseGeometry()
    obj.area()  # This should raise an exception
except Exception as e:
    print(f"[Exception] {e}")

    