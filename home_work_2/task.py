


#checking is it number
number = input("Enter number: ")
while type(number) != int or type(number) != float:
        
        try:
            number = int(number)
            break
        except Exception: 
            number = input('It is not a number! Enter number: ')


if number <= -500:
    print('This number more or equal than -500')

elif number > -500 and number <= -100:
    print('This number more or equal than -100 and less than -500')

elif number > -100 and number < 0:
    print('This number more than 0 and less than -100')

elif number == 0:
    print('This number equal 0')

elif number > 0 and number < 100:
    print('This number more or equal than 0 and less than 100')

elif number > 100 and number < 500:
    print('This number more than 100 and less than 500')

elif number >= 500:
    print('This number more or equal than 500')
