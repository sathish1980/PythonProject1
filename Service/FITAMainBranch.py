from Service.FITA import FITA123



class FITAMainBranch123(FITA123):

    fruits=["apple","orange"]

    def div(self,a,b):
        try:
            c=a/b
            print(c)
            try:
                pass
            except:
                pass
        except ZeroDivisionError:
            print("you have given 0 value in the denominator")
        except:
            print("Error")
        finally:
            print("finally block")

    def get_fruits(self):
        print(self.fruits[2])

    def getCoursedetailsFITA(self):
        print(self.getterCount())
        self.__course123="Python"
        print(self.__course123)

obj = FITAMainBranch123()
obj.div(10,0)
obj.get_fruits()
obj.getCoursedetailsFITA()

