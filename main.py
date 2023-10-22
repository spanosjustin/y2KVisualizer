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

a = turtle.Turtle()
a.speed("fastest")

rand = random.randint(0,1)
randAngle = random.randint(1, 180)

# Color Arrays
colors = ['red', 'dark red']
colorsTwo = ['blue', 'dark blue']
colorsThree = ['violet', 'purple']
colorsFour = ['teal', 'yellow']

running = True

BinaryStringList = ['0', '1']
# Print Binary function
#def PrintBinary(outp):

while running:
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
            box_Vis.right(89*(number+1))
            box_Vis.pencolor(colorsThree[number%2])
        else:
            box_Vis.forward(number-230)
            box_Vis.right(89*(number+1))
            box_Vis.pencolor(colorsThree[number%2])

        if (
            a.xcor() < -turtle.window_width() / 2 or
            a.xcor() < turtle.window_width() / 2 or
            a.xcor() < -turtle.window_height() / 2 or
            a.xcor() < -turtle.window_height() / 2
            ):
            a.forward(number-190)
            a.right(randAngle - (number))
            a.pencolor(colorsFour[number%2])
        else:
            a.forward(500)
            a.right(90)
            a.pencolor(colorsFour[number%2])
    
turtle.bye()
