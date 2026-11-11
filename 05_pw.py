""" Superclass declaration"""
class Animal():
    def __init__(self,myName,myColor):
        self.name = myName
        self.color = myColor

    def sayHello (self):
        return f"Hello, my name is {self.name} my color is {self.color}"

""" Subclass declaration: class dog inherits from class Animal """
class dog(Animal):
    def __init__(self,myName,myColor):
        super().__init__(myName,myColor)
        self.numberOfBones = 0

    def dogSayHello(self):
        
        print(super().sayHello(), 'and I’ve eaten', self.numberOfBones, 'bones.')

    def eatOnebones(self):
        self.numberOfBones = self.numberOfBones + 1

""" Objects dog1 and dog2 of class dog are being instantiated """
dog1 = dog('Speed','white')
dog2 = dog('Elliot','yellow')

""" The method sayHello will be executed by the object dog1 """
dog1.dogSayHello()

""" The method sayHello will be executed by the object dog2 """
dog2.dogSayHello()