import turtle
import random
elsa = turtle.Turtle()
elsa.speed(0)

#set background in grey
turtle.Screen().bgcolor("grey")

#create a list of clours
colours = ["cyan", "purple", "white", "blue", "yellow", "orange", "red", "pink", "green"]

#move the pen in starting position
elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()

#create one branch of the snowflake
def branch():
    for i in range(3):
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)

#draw branch 8 times
for i in range(8):
    branch()
    elsa.color(random.choice(colours))
    elsa.left(45)


    
    