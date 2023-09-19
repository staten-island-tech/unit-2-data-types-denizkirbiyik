import turtle
from turtle import *
t = Turtle()
t.speed(5000)

def Square():
    for i in range(4):
        t.forward(10)
        t.left(90)

def SquareLine(O):
    for i in range(O):
        Square()
        t.forward(10)

def Pyramid(N):
    for i in range(N):
        SquareLine(i)
        t.right(180)
        t.forward(10*i)
        t.left(90)
        t.forward(10)
        t.left(90)
    SquareLine(N)
Pyramid(13)
turtle.done()