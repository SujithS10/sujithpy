from abc import ABC, abstractmethod

class car(ABC):

    @abstractmethod
    def moveFor(self):
        pass

    @abstractmethod
    def moveBac(self):
        pass

    @abstractmethod
    def fm(self):
        pass
    
class swift(car):

    def moveFor(self):
        print("moving for")

    def moveBac(self):
        print("moving bac")

    def fm(self):
        print("playing fm")

my_car = swift()
my_car.moveBac()