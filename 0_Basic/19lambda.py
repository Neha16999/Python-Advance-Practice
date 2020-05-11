my_list=[1,2,3]

print(list(map(lambda item: item*2 , my_list)))
print(my_list)

print(list(map(lambda num: num**2, [1,2,3])))

a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])  #for performing sort on second item

print(a)