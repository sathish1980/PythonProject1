from Service.oops import firstclass


class Fourthclass(firstclass):

    def fourthclassimplementation(self):
        print("fourth class")

obj = Fourthclass()
obj.fourthclassimplementation()
obj.printvalues(1000)
obj.secondclassimplementation()