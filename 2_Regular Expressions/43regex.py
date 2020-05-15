import re

string = 'search this inside of this text please !'


print(re.search('this',string))  #gives match object
a=re.search('this',string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())
   