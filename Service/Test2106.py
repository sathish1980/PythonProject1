from Service.FITA import FITA123


class Test2106(FITA123):

    def details(self):
        print(self.course123)
        self.course123 = "Python"
        print(self.course123)

obj = Test2106()
obj.details()