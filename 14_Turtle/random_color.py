from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed("normal")
tim.pensize(8)

colors = ["navy", "dark olive green", "slate blue", "medium violet red", "dark red", "dark red", "gold"]
direction = [0, 90, 180, 270]

for _ in range(1000):
    tim.forward(30)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()