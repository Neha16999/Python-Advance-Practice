with open('abc.txt', mode='r+') as myfile:
    #print(myfile.readlines())
    text=myfile.write(':)')
    print(text)     #prints no of char


with open('happy.txt', mode='w') as myfile1:
    text1=myfile1.write(':)')
    print(text1)
