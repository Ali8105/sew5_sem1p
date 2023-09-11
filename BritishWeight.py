class BritishWeight():

    lb = 0

    def __init__(self, st=0, lb=0):
        self.lb = st*14
        self.lb += lb



    def __add__(self, other):
        if isinstance(other, BritishWeight):
            return BritishWeight(lb=self.lb + other.lb)



    def __str__(self):
        return str (self.stones) + " stones " +  str(self.lb%14) + " Pounds"

    @property
    def stones(self):
        return self.lb // 14



b = BritishWeight(1,13)
print(b.lb)
a = BritishWeight(2,2)


print(a + b)


