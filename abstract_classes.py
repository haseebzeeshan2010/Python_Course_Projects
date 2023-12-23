from abc import ABC, abstractmethod   #import ABC and method

class Employee(ABC): #Define ABC method

    @abstractmethod  #Decorator function. A decorator is a function that takes another function as its arguments and gives a new function as its output
    def donate(self):
        pass

class Donation(Employee):   #Create sub-class
    def donate(self):
        a = input("How much would you like to donate: ") #Implementation
        return a

#Create instances
amounts = []
john = Donation()
j = john.donate()
amounts.append(j)

peter = Donation()
p = peter.donate()
amounts.append(p)

#Print amounts
print(amounts)