def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

@my_decorator
def hello():
    print('Helloooo')       

@my_decorator
def bye():
    print('see you soon') 


hello()   
bye()  

# work=my_decorator(hello)
# print(work())