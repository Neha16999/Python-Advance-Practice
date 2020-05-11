def fib(no):
    x=0
    y=1
    for nums in range(no):
        yield x
        temp = x
        x=y
        y=temp+y
    

for x in fib(1000):
    print(x)        