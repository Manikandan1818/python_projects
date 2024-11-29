import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.speed("fastest")
color_list=[(252, 251, 248), (245, 251, 250), (253, 249, 252), (242, 245, 248), (139, 80, 53), (185, 163, 125), (138, 166, 176), (60, 111, 134), (17, 42, 73), (139, 62, 88), (162, 153, 44), (66, 119, 101), (147, 182, 171), (215, 210, 107), (76, 34, 29), (69, 151, 163), (115, 39, 32), (96, 145, 119), (177, 148, 162), (74, 30, 35), (168, 99, 127), (33, 56, 105), (104, 123, 165), (107, 40, 49), (175, 106, 90), (209, 181, 194), (21, 96, 86), (169, 202, 196), (9, 97, 112), (220, 178, 172)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    
screen = turtle_module.Screen()
screen.exitonclick()