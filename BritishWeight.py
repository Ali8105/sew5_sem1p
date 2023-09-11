class BritishWeight():

    lb = 0

    def __init__(self, st, lb):
        self.lb = lb


    def __add__(self, other):
        if isinstance(other, BritishWeight):
            b = BritishWeight(self.lb + other.lb)
        return b


    def __str__(self):


    def 


b = BritishWeight(1,2)
print(b)


