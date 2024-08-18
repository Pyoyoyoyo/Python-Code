import turtle
import turtle as t
import random

tim = t.Turtle()

# # Challenge 1 - Draw a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# # Challenge 2 - Draw a Dashed Line ########
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


def make_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# def random_walk():
#     color = random_color()
#     tim.pencolor(color)
#     rotate = [0, 90, 180, 270]
#     tim.setheading(random.choice(rotate))
#     tim.forward(25)


# screen = t.Screen()
# screen.colormode(255)
# tim.speed("fast")
#
# color = make_random_color()
# tim.pencolor(color)
# tim.circle(50)

# for _ in range(100):
#     random_walk()
# Challenge 5 - Spirograph

screen = t.Screen()
screen.colormode(255)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(make_random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


tim.speed("fastest")
draw_spirograph(5)

screen.exitonclick()
