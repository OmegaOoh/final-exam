import copy
import turtle
import random


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Polygon:
    reduction_ratio = 0.618

    def __init__(self, sides, size, orientation, location: Vector, color, bordersize):
        self.sides = sides
        self.size = size
        self.rotation = orientation
        self.location = location
        self.color = color
        self.border = bordersize

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location.x, self.location.y)
        turtle.setheading(self.rotation)
        turtle.color(self.color)
        turtle.pensize(self.border)
        turtle.pendown()
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360 / self.sides)
        turtle.penup()

    def draw_inside(self):
        for _ in range(2):
            # reposition the turtle and get a new location
            turtle.penup()
            turtle.forward(self.size * (1 - Polygon.reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - Polygon.reduction_ratio) / 2)
            turtle.right(90)
            self.location.x = turtle.pos()[0]
            self.location.y = turtle.pos()[1]

            # adjust the size according to the reduction ratio
            self.size *= Polygon.reduction_ratio

            # draw the second polygon embedded inside the original
            self.draw_polygon()


class Drawer:
    @staticmethod
    def get_new_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def __init__(self, num):
        self.num = num

    def rand_draw(self, side, is_embed: bool):
        for _ in range(self.num):
            # draw a polygon at a random location, orientation, color, and borderline thickness
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = Vector(random.randint(-300, 300), random.randint(-200, 200))
            color = self.get_new_color()
            border_size = random.randint(1, 10)
            p = Polygon(side, size, orientation, location, color, border_size)
            p.draw_polygon()
            if is_embed:
                p.draw_inside()


# Initialization
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# Take User Input
choice = input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: ")
while choice not in [str(i) for i in range(1, 9)]:
    choice = input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: ")

if choice == '1':
    d = Drawer(random.randint(25,35))
    d.rand_draw(3, False)
elif choice == '2':
    d = Drawer(random.randint(25,35))
    d.rand_draw(4, False)
elif choice == '3':
    d = Drawer(random.randint(25,35))
    d.rand_draw(5, False)
elif choice == '4':
    for i in range(3,6):
        d = Drawer(random.randint(5,10))
        d.rand_draw(i, False)
elif choice == '5':
    d = Drawer(random.randint(25,35))
    d.rand_draw(3, True)
elif choice == '6':
    d = Drawer(random.randint(25,35))
    d.rand_draw(4, True)
elif choice == '7':
    d = Drawer(random.randint(25,35))
    d.rand_draw(5, True)
elif choice == '8':
    for i in range(3, 6):
        d = Drawer(random.randint(5,10))
        d.rand_draw(i, True)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
