from Service.SecondClass import SecondClass
from Service.oops import firstclass


class Thirdclass(SecondClass,firstclass):

    def thirdclassdetails(self):
        print("third class info")

    def secondclassimplementation1(self):
        print("thirdclass")

    def getDiscountvalues(self):
        taxamount3 = 1000 - self.taxcalculation(1000)
        print("taxamount3:",taxamount3)
        if taxamount3 >1000:
            discount = taxamount3 *.15
            taxamount3 = taxamount3 -discount
        else:
            pass
        print("your final amount  is : ", taxamount3)



td =Thirdclass()
td.thirdclassdetails()
#td.printvalues(1000)
td.secondclassimplementation()
td.getDiscountvalues()