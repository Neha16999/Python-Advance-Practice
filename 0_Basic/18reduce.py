from functools import reduce

my_list=[1,2,3]
def accumulator(acc, item):
    print(acc, item)
    return acc + item   #whatever is returned by this becomes the val of acc

print(reduce(accumulator,my_list,10))
print(my_list)    