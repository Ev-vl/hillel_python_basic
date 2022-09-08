import math
import time
from tkinter import PIESLICE
import test_name_08_09_2022

print('------------------- import test file')
r1 = test_name_08_09_2022.WEATHER

print(f'Name from lesson 2: {r1}')

if __name__ == '__main__':
    # int - целое число
    x1 = 9
    x2 = 2
    y1 = 2.512313
    #print(x1)
    #print(type(x1))
    #str(type(x1))
    #print(type(x1) == int)

    print('--------')
    print(x1*x2)
    print(x1+x2)
    print(x1/x2)
    print(x1-x2)

    print('--------')
    print(x1//x2)
    print(type(x1//x2))

    print('--------')
    print(9 ** (1/2)) # будет 3
    print(9 ** 1/2) # будет 4,5 из-за приоретизации степени, а потом деления на 2
    print(pow(x1, 1/2))

    print('--------')
    print(f'{x1} % {x2} = ',x1 % x2)

    print('-------- ceil - потолок; floor - пол')
    
    print(f'Ceil {math.ceil(y1)}, type {type(math.floor(y1))}')
    print(f'Floor {math.floor(y1)}, type {type(math.floor(y1))}')

    print('-------- round - округление до 2 чисел ПЗ')
    print(f'Round 2: {round(y1, 2)}')
    
    print('-------------------')

    y2 = 2.5168
    y3 = 6.13
    t0 = time.time()
    print(f'Subtract: {y2 - y3}, absolute value: {abs(y2-y3)}')
    print(f'Negative powers of 5: {-5 ** 2} {-5 ** 3} {-5 ** 9}')

    print('------------------- time')
    
    #time.sleep(1)
    print(f'Наша программа выполняется за: {round(time.time() - t0, 4)} с')

    print('------------------- str')
    
    #'Hello there!'.encode('utf-8')
    x1 = x3 = 9
    x3 = 11
    
    print(f'Repr, {repr(x1)}, {repr(x3)}')
    print(f'Repr, {repr(x2)}')

    print('------------------- repr')

    #НАПОМНИТЬ РАЗОБРАТЬ ПОТОМ

    print('------------------- str')

    s = 'Hello there, my friend!'
    print(s.lower())
    print(s.upper())
    #s = 'python'
    print(s.title())
    
    print(s.upper(), s.upper().title())

    print(s.capitalize())

    s="""
        Hello
        there
        how
        are 
        you?
        """
    print(s)

    #можно эксперементировать
    s = '5.0'
    print('Is digit? ', s.isdigit())
    print('Is nubmer? ', s.isnumeric)
    print('Is flot', s.isdecimal)

    
    print('Python_3_'.strip('_'))
    s = input('Введите число х= ')
    
    #-------
    # Не входит в план занятий
    try:
        int(s)
    except Exception:
        print('Это не число')    
    print(s.lstrip('-').isdigit())
    #-------

    print('------------------- str modification')

    s = 'Hello there, my friend!'
    s = s.replace('Hello', 'Hi')
    print(s)
    print(s.find('Hello'), s.rfind('my'))

    #float - дробное число
    
    #print(type(y))
    #print(round(y))
    
    