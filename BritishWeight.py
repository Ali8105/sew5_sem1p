import doctest

__author__ = "Ali Gurbuz"
class BritishWeight():

    """
    Variable nur in Pounds abzuspeichern
    """
    lb = 0

    def __init__(self, st=0, lb=0):
        """
        Konstruktor um Pounds und Stones einzugeben
        :param st: Stones
        :param lb: Pounds
        """
        self.lb += st*14
        self.lb += lb



    def __add__(self, other):
        """
        >>> print(BritishWeight(1,13) + BritishWeight(2,2))
        4 stones 1 Pounds

        >>> print(BritishWeight(1,1) + BritishWeight(2,3))
        3 stones 4 Pounds

        addiert NUR BritishWeight mit BritishWeight
        :param other: Britishweight
        :return: Ergebnis
        """
        if isinstance(other, BritishWeight):
            return BritishWeight(lb=self.lb + other.lb)
        else:
            print("BritishWeight kann nur mit BritishWeight addiert werden!")
            exit()



    def __str__(self):
        return str (self.stones) + " stones " +  str(self.lb%14) + " Pounds"

    @property
    def stones(self):
        return self.lb // 14


if __name__ == '__main__':
    doctest.testmod(verbose=True)



