import random
from turtle import Turtle,Screen

tim=Turtle()
colors=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(sides):
    degree = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.left(degree)

for shape in range(3,11):
       tim.color(random.choice(colors))
       draw_shape(shape)

screen=Screen()
screen.exitonclick()