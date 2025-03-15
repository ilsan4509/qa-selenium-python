#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__

class Calculator:
    num = 100
    #default constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3) #Creating an object of the Calculator class
obj.getData()
print(obj.num)
print(obj.Summation())

obj_1 = Calculator(4, 5)
obj_1.getData()
print(obj_1.num)
print(obj_1.Summation())