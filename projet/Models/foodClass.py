import turtle
import random

from Models.artefactClass import Artefact

class Food(Artefact):
  def __init__(self, color, shape, position):
    super().__init__(color, shape, position)

class Bone(Food):
    def __init__(self, position):
        super().__init__("brown", "bone.gif", position)

class Lettuce(Food):
    def __init__(self, position):
        super().__init__("purple", "lettuce.gif", position)

class Banana(Food):
    def __init__(self, position):
        super().__init__("orange", "banana.gif", position)

class Fish(Food):
    def __init__(self, position):
        super().__init__("blue", "fish.gif", position)
