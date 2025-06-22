fruits=("apple","orange","grapes","mango","grapes","pineapple","orange")

print(fruits)
print(type(fruits))

# retrieve
for eachvalue in fruits:
    print(eachvalue)


for eachval in range(0,len(fruits)): #0,3
    print(fruits[eachval])

#update (its not possible since its unchangable)
#lastvalue=fruits[-1]
#fruits[len(fruits)-1]=lastvalue+"test"
#print(fruits)

#remove (remove ,pop ,del)
#fruits.remove("orange")
#fruits.pop()
print(fruits)
grapescount = fruits.index("pineapple")
print(grapescount)
listofvalues= list(fruits)
print(type(listofvalues))
