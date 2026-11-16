import turtle  # Imports the turtle graphics module to create drawings and animations

# Set up Turtle window
window = turtle.Screen()  # Creates the graphics window (canvas) object
window.title("Turtle Graphics")  # Sets the title displayed at the top of the window
window.bgcolor("white")  # Sets the background color of the window to white

turtle.register_shape("dog.gif")  # Registers a custom GIF image so it can be used as a turtle shape

dog = turtle.Turtle()  # Creates a new Turtle object named 'dog'
dog.shape("dog.gif")  # Changes the appearance of the 'dog' cursor to the registered 'dog.gif' image
dog.penup()  # Lifts the pen so the 'dog' moves without drawing a line behind it
dog.speed(1)  # Sets the movement animation speed to 1 (slowest visible speed)
dog.forward(200)  # Moves the 'dog' forward by 200 pixels in the direction it is facing

window.exitonclick()  # Keeps the graphics window open until the user clicks inside it