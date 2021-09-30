import main as c


class FooCalculator:

    # empty constructor
    def __init__(self):
        pass

    def sum(self,m,n):
        return c.sum(m,n)

    def divide(self,m,n):
        return c.divide(m,n)

x = FooCalculator()
print("sum: "+str(x.sum(5,4)))