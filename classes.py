#---------------start of example-------------

class Recipe():
    # init(constructor) takes the objects created using the new method along with other arguments to initialize the new object being created

    def __init__(self) -> None:
        pass

#----------------end of example--------------

class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    
    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid" + str(self.amount)
        else:
            return self.name + " is not paid yet"

nathan = Payslips("Nathan", "no", 1000)
roger = Payslips("Roger", "no", 3000)

print(nathan.status(), "\n", roger.status())

nathan.pay()
print("After payment")
print(nathan.status(), "\n", roger.status())


#--------------multi-level-inheritance-----------

class A:  #parent class
    a = 1

class B(A): #child of A, but parent of C
    a = 2

class C(B): #Child of B
    pass

c = C()
print(c.a)