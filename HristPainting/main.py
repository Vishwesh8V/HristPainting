import turtle as t
import random
from turtle import Turtle, Screen
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim = Turtle()
tim.penup()
tim.back(200)
tim.right(90)
tim.forward(200)
tim.left(90)
tim.hideturtle()
for _ in range(10):
    for _ in range(10):
        tim.pendown()
        tim.dot(20, "#" + "%02x%02x%02x" % random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.penup()
    tim.back(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)

screen = Screen()
screen.exitonclick()