while True:
    try:
        age=int(input("enter a number "))
        10/age
    except ValueError:
        print('Please enter a number ')
    except ZeroDivisionError:
        print('Enter non zero number ')
    else:
        print('Thank you !')
        break            



