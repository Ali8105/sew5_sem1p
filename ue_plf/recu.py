def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)


print(factorial(5))


def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number-1) + fib(number-2)

print(fib(5))



def rec1(num):
    if num < 10:
        return num
    else:
        return 1+rec1(num/10)

print(rec1(1000))


def zahlen(wert):
    x = 0
    munzen = [0.01,0.02,0.05,0.10,0.20,0.5,1.0,2.0]
    for munze in munzen:
        if munze < wert:
            x += zahlen(float(wert-munze))
    return x + 1

print(zahlen(0.10))



def ar():
    my_ar = [[None]*10 for _ in range(10)]
    for i in range (10):
        for y in range(10):
            my_ar[i][y] = "hallo " + str(y) + str(i)
    print(my_ar)

ar()










