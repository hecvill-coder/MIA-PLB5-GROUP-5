import turtle
import random

class Artefact:

  def __init__(self, color, shape, position):
    self.turtle = turtle.Turtle()
    self.turtle.shape(shape)
    self.turtle.color(color)
    self.turtle.penup()
    self.turtle.goto(position)
    self.position = position

  def get_position(self):
    return self.position

  def hide(self):
    self.turtle.hideturtle()