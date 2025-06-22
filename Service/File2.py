age="75" # global variable
#global course
course ="java"
salary=2000
Salary=5000
age1,age2,age3=20,30,60
#age6,age4,age5=70

print(2+3)
print(3+5)
print(100+10)

"""
this functiona is use to add 2 numbers
"""
def addition(a,b):
    age="30" # local variable
    print("my age is "+age)
    print(a-b)

def subtraction():
    age="99"
    print("my age is " + age)


addition(20,20)
addition(10,20)
addition(30,20)
subtraction()

newsalary="My Salary is :"+str(salary)
print(newsalary)
print(type(age))
print("My age is :"+age)
print("My age is : ",age)
hdfbsf="60"
print('Fita + technology'+ hdfbsf)

"""
Function - 4types
1.Function with parameter / arguments
2.Function wihtout parameter / arguments
3.Funciton with return type
4.Funcitonal with out return type

syntax : def functionname():
"""

#1.Function with parameter / arguments
def PrintMyData(name,age,salary):
    print("myname is : "+name)
    print("my age is : ", age)
    print(salary)

def multiply(a,b):
    result = a*b
    return result

#2.Function without parameter / arguments and with out return type
def PrintMyOldData():
    print("myname is : sathish")
    print("my age is : 50")
    print(2000)



PrintMyData("Sathish","79",1000)
multiply(5,10)
PrintMyOldData()
def findLengthOfFita(name,first,second):
    output = multiply(first,second)
    next5 =output+5
    #next5 = multiply(first,second)+5
    print(next5)
    totalLenght = len(name)
    print(totalLenght)

def PrintMyFavFood():
    myFavFood = input("Enter your fav Food: ")
    f =input("enter first number: ")
    s= input("enter secnd number")
    output=int(f)+int(s)
    print(output)
    print("Hey nice t0  hear that your fav food is ",myFavFood ," and I too like it")


firstValue =150
secondValue=300

if firstValue>secondValue:
    print("firstvalue is greater than secnod value",firstValue,"is greater than",secondValue)
    if firstValue >500 and firstValue<2000:
        print("firstvalue is greater than 500")
        if firstValue>1000:
            pass
elif firstValue>200:
    print("first value is greater than 200")
elif firstValue>150 or (firstValue<200 and firstValue>150):
    print("first value is greater than 150")
elif firstValue>100 and firstValue<=150:
    print("first value is between 100 to 150")
else:
    print("firstvalue is lesser than secnod value")


print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)

i=1
print(type(i))
while i<8 and i>0:

    if i==5 or i==7:
        #i=i*5
        i = i + 1
        #print("new value", i)
        #break
        continue
    print("while : ", i)
    i=i+1


print("final line")

fruits=["apple","orange","grapes","mango"]
print(fruits)
identified =False
expectedfruit = input("Enter the fruit name: ")
for eachfruits in fruits:
    if eachfruits==expectedfruit:
        print(expectedfruit, " is available in rack2")
        identified=True
        break
if(identified==False):
    print("the given fruit is not available")

Age=[1,34,56,78,99]
for eachage in Age:
    print(eachage)
for eachvalue in range(100,108):
    print(eachvalue)
    #print(eachfruits)

for eachvalue1 in range(1,5):
    print("**********")
    print(eachvalue1)
    for eachvalue2 in range(100,105):
        print(eachvalue2)
#findLengthOfFita("FITA",5,5)
#PrintMyFavFood()


