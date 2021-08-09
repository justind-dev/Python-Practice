class Point:
    default_color = "red"
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        pass
    
    def draw(self):
        print(f"Point ({self.x} , {self.y})")
        print(f"Default color: {self.default_color}")

point = Point(1,2)
point.draw()