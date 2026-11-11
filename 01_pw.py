""" Class declaration """
class Cat():
    def __init__(self,myName):
        self.name = myName 
        self.color = 'white'

    def sayHello (self):
        print('Hello, my name is',self.name,'and my color is',self.color)

""" Object cat1 of class Cat is being instantiated """
cat1 = Cat('Speed')

""" The method sayHello will be executed by the object cat1 """
cat1.sayHello()
