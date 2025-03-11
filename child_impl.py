from oop_examples import Calculator


class ChildImpl(Calculator):
    num2=200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData (self):
        print("@@@@@@@@@@@@@@@@")
        print(self.num2)
        print(self.num)
        print(self.Summation())
        print("@@@@@@@@@@@@@@@@@")
        return self.num2 + self.num + self.Summation()

obj = ChildImpl()
print(obj.getCompleteData())




