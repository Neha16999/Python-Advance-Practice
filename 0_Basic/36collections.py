from collections import Counter, defaultdict, OrderedDict

li=[1,2,3,4,5,6,7,8,7]
sentence="Hare Krishna hare krishna krishna krishna hare hare Hare Rama hare rama rama rama hare hare"
print(Counter(li))  #shows no of occurance
print(Counter(sentence))

dictionary=defaultdict(lambda : 'does no exsist', {'a':1, 'b':'2'})
print(dictionary['c'])

d1=OrderedDict()
d1['a']=1
d1['b']=2

d2=OrderedDict()
d2['b']=2
d2['a']=1

print(d1==d2)
