from Models.artefactClass import Artefact

class Obstacle(Artefact):
    def __init__(self, shape, position):
        super().__init__("white", shape, position)

class Fence(Obstacle):
    def __init__(self, position):
        super().__init__("fence.gif", position)

