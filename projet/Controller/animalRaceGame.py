#Import all the files, be careful here there will be a lot of errors
from Models.animalClass import Monkey
from Models.animalClass import Dog
from Models.animalClass import Pinguin
from Models.animalClass import TurtleRacer
from Models.foodClass import Lettuce
from Models.foodClass import Banana
from Models.foodClass import Fish
from Models.foodClass import Bone
from Models.obstacleClass import Fence
from Models.raceTrackClass import RaceTrack
import random


class AnimalRaceGame:
    def __init__(self):
        self.track = RaceTrack(1000, 300)
        self.finish_line = 450

    def create_animals(self):
        monkey = Monkey((-450, 75))
        dog = Dog((-450, 25))
        turtle_racer = TurtleRacer((-450, -25))
        pinguin = Pinguin((-450, -75))
        return monkey, dog, turtle_racer, pinguin

    def create_food_items(self, num_items):
        starting_line = -(self.track.width // 2) + 50
        finish_line = (self.track.width // 2) - 50
        food_classes = [Bone, Lettuce, Banana, Fish]
        foods = [random.choice(food_classes)((random.randint(starting_line, finish_line), random.choice([75,25,-25,-75]))) for _ in range(num_items)]
        return foods

    def create_obstacle_items(self, num_items):
            starting_line = -(self.track.width // 2) + 50
            finish_line = (self.track.width // 2) - 50
            obstacle_classes = [Fence]
            obstacle = [random.choice(obstacle_classes)((random.randint(starting_line, finish_line), random.choice([75,25,-25,-75]))) for _ in range(num_items)]
            return obstacle   