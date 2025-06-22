from Service.oops import firstclass


class SecondClass():

    taxamount=0

    def __init__(self):
        tax=0.15
        print(tax)
        self.taxamount=tax
        #return tax

    def secondclassimplementation(self):
        print("secondclass")
        print(self.taxamount)

    def secondclassimplementation(self):
        print("secondclass 2nd time")
        print(self.taxamount)

#sc = SecondClass(0.15)
#sc.printvalues(1000)
#sc.secondclassimplementation()
"""sc.secondclassimplementation()

fc=firstclass()
print(fc.age)
fc.printvalues(1000)"""

