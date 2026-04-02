class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y: # other is a variable pointing to an object of the Coordinate class any Coordinate has object .x and .y (.x .y can be any value)
            return True
        else:
            return False
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y) # creates a new coordinate object of the sums of x and y values respectively

    def __str__(self):
        return f"({self.x}, {self.y})"


# tests
p1 = Coordinate(2, 4)
p2 = Coordinate(3, 7)
p3 = Coordinate(2, 4)
p4 = p1 + p2
print("p1 == p2?", p1 == p2)
print("p1 == p3?", p1 == p3)
print(f"{p1} + {p2} = {p4}")
print(p1)

# can do self 
