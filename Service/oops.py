class firstclass():
    print("My name is sathish")
    age =15
    def taxcalculation(self,amount):
        taxamount = amount * 0.15
        print("your tax amount is: ", taxamount)
        return taxamount

    def printvalues(self,amount):
        taxamount = self.taxcalculation(amount)
        food1 = {"idly": 7, "dosa": 45, "pongal": 30}
        total = 0
        print(food1.values())
        for eachvalue in food1.values():
            total = eachvalue + total
        print("total values: ", total )
        print("final values: ", total+taxamount)

#fc=firstclass()
#fc.taxcalculation(1000)
#fc.printvalues(1000)
