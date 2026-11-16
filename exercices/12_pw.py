import turtle  # Imports the turtle graphics module for drawing

pen = turtle.Turtle()  # Creates a Turtle object (the cursor/pen) named 'pen'

def square(side):  # Defines a function named 'square' taking the side length 'side' as a parameter
    for i in range(4):  # Loops 4 times (once for each side of the square)
        pen.forward(side)  # Moves the pen forward by 'side' pixels
        pen.right(90)  # Turns the pen 90 degrees to the right

pen.fillcolor("red")  # Sets the fill color for shapes to red
pen.begin_fill()  # Tells turtle to start recording the shape to be filled
square(150)  # Calls the 'square' function to draw a square with sides of 150 pixels
pen.end_fill()  # Stops recording and fills the interior of the square with red
pen.hideturtle()  # Hides the turtle cursor (arrow) from the screen
turtle.done()  # Keeps the graphics window open until the user closes it