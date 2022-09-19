#----------- Quadrilateral check -----------#


from operator import truediv
from tkinter import PIESLICE


def input_value(name):
    num = input(f'Enter {name}: ')
    while True:
        try:
            num = float(num)
            if num > 0:
                return num
        except Exception: 
            input(f'It is not a wrong value! Enter {name}: ')

def foursquare_check(a,b,c,d):
    if a == b == c == d:
        return True

def rectangle_check(a,b,c,d):
    #continue

if __name__ == '__main__':
    
    print('Hello! Please, input quadrilateral values: ')

    a = input_value('a')
    b = input_value('b')
    c = input_value('c')
    d = input_value('d')

    if foursquare_check(a,b,c,d):
        print('It is foursquare!')