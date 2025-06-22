from Service.Overloading import overloading


class overriding(overloading):

    def sub(self,a,b):
        c=a-b
        print(c)

    def add1(self,w,e,r):
        z=w+e-r
        print("overriding: ",z)
obj= overriding()
obj.sub(5,3)
obj.add(1,2,3)