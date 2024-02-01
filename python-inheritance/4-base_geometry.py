class BaseGeometry:
    def area(self):
        raise NotImplementedError("area() is not implemented")

# Create an instance of BaseGeometry
bg = BaseGeometry()

# Try to print the result of bg.area()
try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
