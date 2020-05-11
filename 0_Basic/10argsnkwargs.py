def fun(*args, **kwargs):
    print(args)
    print(kwargs)
    total=0
    for item in kwargs.values():
        total=total+ item
    return total + sum(args)    


print(fun(1,2,3,4,5,num1=6,num2=7))    