import os
import turtle

script_dir = os.path.dirname(os.path.abspath(__file__))
dog_image_path = os.path.join(script_dir, "dog.gif")
cat_image_path = os.path.join(script_dir, "cat.gif")
mouse_image_path = os.path.join(script_dir, "mouse.gif")

window = turtle.Screen()
window.title("Turtle Graphics")
window.bgcolor("white")

# 1. Enregistrer les 3 formes (images)
turtle.register_shape(dog_image_path)
turtle.register_shape(cat_image_path)
turtle.register_shape(mouse_image_path)


dog = turtle.Turtle()
dog.shape(dog_image_path)
dog.penup()
dog.goto(-400, 0)    
cat = turtle.Turtle()
cat.shape(cat_image_path)
cat.penup()
cat.goto(-200, 0) 

mouse = turtle.Turtle()
mouse.shape(mouse_image_path)
mouse.penup()
mouse.goto(0, 0) 

mouse.speed(1)
cat.speed(1)
dog.speed(1)



for _ in range(40):
    mouse.forward(5)
    cat.forward(5)
    dog.forward(5)



window.exitonclick()