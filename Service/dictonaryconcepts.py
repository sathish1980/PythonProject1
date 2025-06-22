fruits={1:"apple",2:"orange",3:"grapes",4:"mango",5:"grapes",6:"pineapple",7:"orange",6:"banana"}
bankdetails={"name":"sathish","age":"17","accno":"143343434","bal":"12000"}
print(fruits)
print(type(fruits))
print(fruits.items())
print(fruits.keys())
print(fruits.values())
print(len(fruits))
print(fruits[4])
#print(bankdetails["newbala"])
print(bankdetails.get("bal"))
bankdetails["age"]="50"
print(bankdetails)
bankdetails.update({"accno":"101010"})
print(bankdetails)

foodlist =["idly","dosa","pongal"]
food ={"idly":7,"dosa":45,"pongal":30} # for eachvalue in food: if eachvalue == ""
totalamount=0
i=0
while (i<10):
    userinput = input("Enter your food")
    if userinput in food :
        quantity = input ("enter quantity:")
        foodvalue =food.get(userinput.lower())
        newtotalamount = int(quantity)*foodvalue
        totalamount =newtotalamount+totalamount
        taxamount = totalamount*.10
        if totalamount>2000:
            discountamount = totalamount*0.15
            finalamount = totalamount-discountamount+taxamount
        else:
            finalamount =totalamount+taxamount
    else:
        print("the requested food is not available")

    i=i+1

    print("Please pay : Rs. ",totalamount)

food1 ={"idly":7,"dosa":45,"pongal":30}
total=0
print(food1.values())
for eachvalue in food1.values():
    total =eachvalue+total
print("total values: ",total)