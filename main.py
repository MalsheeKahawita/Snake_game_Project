#import packages
import turtle
import random
import time

#creating playground
playgrnd = turtle.Screen()
playgrnd.title("Snake Game")
playgrnd.setup(width=800,height=800)
playgrnd.tracer(0)
playgrnd.bgcolor('#1d1d1d')

#creating border
turtle.speed(5)
turtle.pensize(4)#border width
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")#border color
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#score
score = 0;
delay = 0.1

#snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("blue")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'



