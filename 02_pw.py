""" Class declaration """
class Cat():
    def __init__(self,myName,myColor):
        self.name = myName
        self.color = myColor
        self.numberOfMice  = int(0)

    def eatOneMouse(self):
        self.numberOfMice += 1

    def sayHello (self):
        print('Hello, my name is',self.name,'my color is', self.color,"and I've eaten",self.numberOfMice,"mouses today")

""" Objects cat1 and cat2 of class Cat are being instantiated """
cat1 = Cat('Speed','white')
cat2 = Cat('Elliot','Red')
cat3 = Cat('Félix','Yellow')

""" The method sayHello will be executed by the object cat1 """
cat1.sayHello()

""" The method sayHello will be executed by the object cat2 """
cat2.sayHello()

cat3.sayHello()
cat3.eatOneMouse()
cat3.sayHello()