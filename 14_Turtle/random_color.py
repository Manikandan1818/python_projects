from turtle import Turtle, Screen
import random
import turtle


tim = Turtle()
turtle.colormode(255)
tim.speed("normal")
tim.pensize(8)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

direction = [0, 90, 180, 270]

for _ in range(1000):
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()