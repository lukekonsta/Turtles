import turtle
from turtle import *

def draw_mini_square(some_turtle):

    counter = 0
    while(counter<4):
        some_turtle.forward(100)
        some_turtle.right(90)
        counter+=1


def draw_square():

    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("blue")
    brad.speed('fast')

    counter = 0
    while(counter<37):
        draw_mini_square(brad)
        brad.right(10)
        counter+=1


def draw_circle():

    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("red")
    angie.speed('slow')
    angie.circle(50)



def draw_triangle():

    roben = turtle.Turtle()
    roben.shape("arrow")
    roben.color("yellow")
    roben.speed('slow')

    roben.forward(100)
    roben.left(90)
    roben.forward(100)
    roben.left(135)
    roben.forward(170)





window = turtle.Screen()#create the background
window.screensize(400,300)
window.bgcolor("orange")
draw_square()
draw_circle()
draw_triangle()
window.exitonclick()#must be placed at the end
