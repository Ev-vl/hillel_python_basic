#ветвление, условия
#conditional exrpessions

if 2+2 == 4: 
    print('Законы математики соблюдены')
else:
    print('Математика не работает')

a = 5
b = 7

if a> b:
    print(f'{a} больше {b}')
else:
    print(f'{a} меньше {b}')

print(a>b)

g = True
f = False

print(f'{type(a>b)=}')
print(f'{g} {type(g)=}')
print(f'{f} {type(f)=}')

h = 0.0
if h:
    print('g is true')
else:
    print('h is false')


color = 'yellow'
price = 8.0

if color == 'yellow'and price < 10:
        print('Ok')
else:
    print('Not ok')

#оператор in - как в SQL

order = 'tea and food'

if 'tea' in order.lower():
    print('good order')

elif 'coffee' in order.lower():
    print('good')
else:
    print('not good')



#процесс написание калькулятора

def return_params():
    a = input('Enter firts number: ')
    b = input('Enter second number: ')
    a = int(a)
    b = int(b)
    return a,b


exit = False

while not exit:
    
    print("""
This is calculator

1. +
2. -
3. *
4. /
5. Exit
    """)
    
    a,b = return_params()
    choise = input('Choise math operation: ')

    if choise == '1' or '+':
        print(f'{a} + {b} = {a+b}')
    elif choise == '2' or '-':
        print(f'{a} - {b} = {a-b}')
    elif choise == '3' or '*':
        print(f'{a} * {b} = {a*b}')
    elif choise == '4' or '/':
        print(f'{a} / {b} = {a/b}')
    elif choise == '5' or 'exit' or 'Exit':
        print('Done.')
        break
    else:
        print('Wrond value')