import turtle
import random
turtle.bgcolor('black')

# Define Visuals
t = turtle.Turtle()
t.speed("fastest")

f = turtle.Turtle()
f.speed("fastest")

box_Vis = turtle.Turtle()
box_Vis.speed("fastest")

# Color Arrays
colors = ['red', 'dark red']
colorsTwo = ['blue', 'dark blue']
colorsThree = ['violet', 'purple']

BinaryStringList = ['0', '1']
# Print Binary function
#def PrintBinary(outp):

for number in range(400):
    t.forward(number+100)
    t.right(number+105/2)
    t.pencolor(colors[number%2])
    
    f.forward(number+150)
    f.right(205)
    f.pencolor(colorsTwo[number%2])

    if (
        box_Vis.xcor() < -turtle.window_width() / 2 or
        box_Vis.xcor() < turtle.window_width() / 2 or
        box_Vis.xcor() < -turtle.window_height() / 2 or
        box_Vis.xcor() < -turtle.window_height() / 2
        ):
        box_Vis.forward(number-230)
        box_Vis.right(89*(number-1))
        box_Vis.pencolor(colorsThree[number%2])
    else:
        box_Vis.forward(number-230)
        box_Vis.right(89*(number+1))
        box_Vis.pencolor(colorsThree[number%2])
    
turtle.done()
