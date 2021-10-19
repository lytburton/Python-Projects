


from abc import ABC, abstractmethod

#Created a class that utilizes the concept of abstraction
#class contains at least one abstract method and one regular method
class Animals(ABC):
    def numAnimals(self,count):
        print("Number of Animals: ",count)

    @abstractmethod
    def AnimalCount(self,count):
        pass
#Created a child class that defines the implementation of its parents abstract method
class ZooAnimals(Animals):
    def AnimalCount(self,count):
        print("There are {} animals at the zoo".format(count))





if __name__ == "__main__":
    
#Created an object that utilizes both the parent and child methods
    pet = ZooAnimals()
    pet.numAnimals("25")
    pet.AnimalCount("16")







