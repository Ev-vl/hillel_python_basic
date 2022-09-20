#----------- Check number range -----------#


#input and float/int check; after checking num will return
def return_float():
    num = input(f'Enter number: ')
    while type(num) != int or type(num) != float:
            
            try:
                num = float(num)
                return num
            except Exception: 
                num = input(f'It is not a number! Enter number: ')



#checking is it number
number = return_float()


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
