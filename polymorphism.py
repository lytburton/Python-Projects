


"""polymorphism.py: This script creates two classes that inherit
                    from another class using Python 3"""



__author__ = "Lyttia Burton"
__version__ = 1.0



"""
Requirements:

Each child should have at least two of their own attributes.

The parent class should have at least one method (function).

Both child classes should utilize polymorphism on the parent class method.
"""

class Parent:
    def __init__(self, name, age, fav_snack): #initializes attributes for this class
        self.name = name
        self.age = age
        self.fav_snack = fav_snack

    def phrase(self): #parent class method
        print("When I was your age, I loved to eat {}.".format(self.fav_snack))


class Child1(Parent):
    def __init__(self, name, age, fav_snack,grade,fav_show): #initializes attributes for this class
        super().__init__(name, age, fav_snack) #allows this child class to inherit the parent class attributes
        self.grade = grade #child class contains two attributes
        self.fav_show = fav_show

    def phrase(self): #child class method using polymorphism
        print("When I start the {} grade I'll still be {} years old!".format(self.grade,self.age))

class Child2(Parent):
    def __init__(self, name, age, fav_snack, sport, best_friend): #initializes attributes for this class
        super().__init__(name, age, fav_snack) #allows this child class to inherit the parent class attributes
        self.sport = sport #child class contains two attributes
        self.best_friend = best_friend
        
        
    def phrase(self):#child class method using polymorphism
        print("I'll be so glad when {} comes over so we can go to the {} game!".format(self.best_friend, self.sport))



if __name__ == "__main__":

    #assigning values to objects p, c1 and c2
    p = Parent('John',45,'chips and salsa')
    c1 = Child1('Brayden',7,'Oreos', '4th', 'Bob the Builder')
    c2 = Child2('Brittany',9,'Cheetos', 'Volleyball','Samantha')

    #calls functions from each class 
    p.phrase()
    c1.phrase() #uses polymorphism
    c2.phrase() #uses polymorphism



    

