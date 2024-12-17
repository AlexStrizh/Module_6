import math

class Figure:
    sides_count = 0
    def __init__(self, color):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *new_sides):
        for side in new_sides:
            if len(new_sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color)
        self.__radius = circumference / (2 * math.pi)
        self.set_sides(circumference)

    def get_square(self):
        return (self.__radius ** 2) * math.pi

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.set_sides()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, rib_length):
        super().__init__(color)
        self.set_sides(*[rib_length] * self.sides_count)

    def get_volume(self):
        rib_length = self.get_sides()[0]
        return  rib_length ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
