try:
    with open ('sad.txt', mode='x')as myfile:
        print(myfile.read())
except FileNotFoundError as err:
    print('File does not exsits')
    raise err
except IOError as err:
    print('IO error')   
    raise err    