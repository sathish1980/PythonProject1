from logging import lastResort

from Service.File2 import fruits

fruits=["apple","orange","grapes","mango","grapes","pineapple","orange"]
newfruits=["berry","dragonfruit"]
print(fruits)
print(type(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1]) #
print(fruits[len(fruits)-1])
print(len(fruits))
print(fruits[1:4])

# retrieve
for eachvalue in fruits:
    print(eachvalue)


for eachval in range(0,len(fruits)): #0,3
    print(fruits[eachval])

"""fruitslist = input("Enter frutis name: ")
if fruitslist not in fruits: #
    print("yes its available")
else:
    print("its not available")"""

#update (index ,append ,extend)
lastvalue=fruits[-1]
fruits[len(fruits)-1]=lastvalue+"test"
print(fruits)
#add in to a specific position
fruits.insert(10,"banana")
print(fruits)
fruits.append("last value")
print(fruits)
fruits.extend(newfruits)
print(newfruits)
print(fruits)

#remove (remove ,pop ,del)
#fruits.remove("assd")
fruits.pop()
print(fruits)
beforedelete = fruits.copy()
print(beforedelete)
#fruits.clear()
#del fruits
fruits.sort(reverse= True)
print(fruits)

invoice=[]
for eachvalue in range(0,100000000):
    userinput = input("Enter product name: ")
    if userinput == "stop":
        break
    else:
        invoice.append(userinput)

print(invoice)
for eachvalue in invoice:
    print(eachvalue)
