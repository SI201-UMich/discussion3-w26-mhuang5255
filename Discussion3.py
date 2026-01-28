import math

class Rectangle():
    # Create the constructor "__init__" method

    # YOUR CODE HERE
    def __init__(self, width, height):
        self.height = height
        self.width = width

    # Create the "__str__" method

    # YOUR CODE HERE
    def __str__(self):
        return f"A rectangle with width {self.width} and height {self.height}"



    # Create the "area_calculator" method

    # YOUR CODE HERE
    def area_calculator(self):
        return self.width * self.height


    # Create the "__eq__" method
    # 
    # Returns a boolean value

    # YOUR CODE HERE
    def __eq__(self, other):
        return self.height == other.height and self.width == other.width



def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print("r1 == r2?")
    print(r1 == r2)
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    r3 = Rectangle(3.0, 3.0)
    print("r3 Area:", r3.area_calculator())
    r4 = Rectangle(4.5, 2)
    print("r3 Area:", r4.area_calculator())
    print("r3 == r4?:", r3 == r4)
    pass

if __name__ == "__main__":
    main()