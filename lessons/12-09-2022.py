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



#процесс написание калькулятора ---- Всё пройдено

