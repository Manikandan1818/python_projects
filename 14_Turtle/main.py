from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("dark olive green")

timmy_the_turtle.speed("slowest")

# for _ in range(8):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(45)

for _ in range(18):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    


screen = Screen()
screen.exitonclick()