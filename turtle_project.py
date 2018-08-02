import turtle
from turtle import *

def draw_l():

    lukas = turtle.Turtle()
    lukas.penup()
    lukas.setx(-100)
    lukas.sety(0)
    lukas.shape("classic")
    lukas.color("blue")
    lukas.speed('normal')
    lukas.pendown()
    lukas.backward(90)
    lukas.left(90)
    lukas.forward(100)

def draw_u():

    luke = turtle.Turtle()
    luke.penup()
    luke.setx(-50)
    luke.sety(100)
    luke.shape("turtle")
    luke.color("white")
    luke.speed('normal')
    luke.pendown()
    luke.right(90)
    luke.forward(100)
    luke.left(90)
    luke.forward(80)
    luke.left(90)
    luke.forward(100)

def draw_k():

    luk = turtle.Turtle()
    luk.penup()
    luk.setx(50)
    luk.sety(100)
    luk.shape("arrow")
    luk.color("red")
    luk.speed('fast')
    luk.pendown()
    luk.right(90)
    luk.forward(100)
    luk.backward(50)
    luk.left(120)
    luk.forward(50)
    luk.backward(50)
    luk.right(90)
    luk.forward(50)
    luk.backward(50)

def draw_e():

    luck = turtle.Turtle()
    luck.penup()
    luck.setx(100)
    luck.sety(50)  
    luck.shape("triangle")
    luck.color("yellow")
    luck.speed('fast')
    luck.pendown()
    luck.forward(50)
    for x in range(180):
        luck.forward(1)
        luck.left(2)
    luck.right(30)
    luck.forward(50)



window = turtle.Screen()#create the background
window.screensize(400,300)
window.bgcolor("orange")
draw_l()
draw_u()
draw_k()
draw_e()
window.exitonclick()#must be placed at the end
