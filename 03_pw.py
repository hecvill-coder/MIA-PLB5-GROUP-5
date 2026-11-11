""" Class declaration """
class Dog():
    def __init__(self,myName,myColor):
        self.name = myName
        self.color = myColor
        self.numberOfBones  = int(0)

    def eatOneMouse(self):
        self.numberOfBones += 1

    def sayHello (self):
        print('Hello, my name is',self.name,'my color is', self.color,"and I've eaten",self.numberOfBones,"mouses today")

""" Objects Dog1 and Dog2 of class Dog are being instantiated """
dog1 = Dog('Speed','white')
dog2 = Dog('Elliot','Red')
dog3 = Dog('Félix','Yellow')

""" The method sayHello will be executed by the object Dog1 """
dog1.sayHello()

""" The method sayHello will be executed by the object Dog2 """
dog2.sayHello()

dog3.sayHello()
dog3.eatOneMouse()
dog3.sayHello()