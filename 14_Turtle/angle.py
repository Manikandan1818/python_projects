from turtle import Turtle
import random

tim = Turtle()
tim.speed("slowest")

colors = ["navy", "dark olive green", "slate blue", "medium violet red", "dark red", "dark red", "gold"]

def draw_shape(num_sides):
    """Get number of sides and color."""
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        
for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()