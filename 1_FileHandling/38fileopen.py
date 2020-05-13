myfile=open('abc.txt')
print(myfile)
print(myfile.read())
myfile.seek(0)      #seek moves the cursor to the position
print(myfile.read())
print(myfile.read())        #prints nothing as cursor is at the end of file

myfile.seek(0)      #seek is must otherwise prints nothing
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())

myfile.seek(0)      #seek is must otherwise prints empty list
print(myfile.readlines())  #prints list of lines

myfile.close()
