# 4-base_geometry.py
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    def area(self):
        """Raises an exception with the message 'area() is not implemented.'"""
        raise Exception("area() is not implemented")

# Test the implementation
try:
    # Instantiate an object of BaseGeometry
    geometry = BaseGeometry()

    # Call the area() method, which will raise an exception
    geometry.area()

except Exception as e:
    # Print the expected output
    print(f"[Exception] {e}")

# Print the attributes of the object (as per the test case)
print(dir(geometry))
