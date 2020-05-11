sample_dict={
    'a':1,
    'b':2,
    'c':3

}


my_dict={k:v**2 for k,v in sample_dict.items()}
my_dict1={k:v**2 for k,v in sample_dict.items() if v % 2==0}
my_dict2={num:num*2 for num in range(5)}
my_dict3={num:num//10 for num in [78,95,88]}

print(my_dict)
print(my_dict1)
print(my_dict2)
print(my_dict3)