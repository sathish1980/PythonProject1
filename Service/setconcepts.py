fruits={"apple","orange","grapes","mango","grapes","pineapple","orange"}
print(fruits)
print(type(fruits))

# retrieve
for eachvalue in fruits:
    print(eachvalue)
if "apple" in fruits:
    print("yes")

fruits.add("gova")
print(fruits)
#fruits.remove("orange")
fruits.discard("adsd")
print(fruits)
fruits.pop()
print(fruits)

value1={"A","B","C"}
value2={"A","Z","D","B"}

"""value3= value1.difference(value2)
print(value3)
value1.difference_update(value2)
print(value1)"""

value3= value1.intersection(value2)
print(value3)
#value1.intersection_update(value2)
#print(value1)

exist = value1.issubset(value2)
print(exist)
exist1 = value1.issuperset(value2)# all the value2 values are exist in value 1

diff = value1.symmetric_difference(value2)
print(diff)