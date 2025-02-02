from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("crimson")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Choose your turtle Colors", prompt="Enter color turtle will win? Purple, Green, Orange, Red, Yellow, Crimson")
colors = ["purple", "green", "orange", "maroon", "yellow", "gray"]
y_position = [-70, -40, -10, 20, 50, 80]

is_race_on = False

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()