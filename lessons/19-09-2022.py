from operator import le
from turtle import pen


x = [
        5, 
        6, 
        7.0, 
        'my name is', 
        [0, 2, True]
    ]
print(x)
print(type(x))

print(x[0])
print(x[1])
print(x[-1]) #last element

print('List length: ', len(x))

y = [4, 5, 6, 2, -5, 5000, 43, 40]

#dynamic work with list, length not matter
for element in y: #for every element in list
    print(element ** 2, end=', ')

print('\n', y)

y = [4, 5, 6, 2, -5, 5000, 43, 40]
y_power_two = list()

#dynamic work with list, length not matter
for element in y: #for every element in list
    y_power_two.append(element ** 2)

print(y, y_power_two)

#calculate sum of elements
y = [2, -7, -5, 400, 60, -400]
summa = 0
for element in y:
    summa += element
print(summa)
print(sum(y)) #function for sum


iterator = 0
f1 = list()
for element in y:
    print(f'{element} это {iterator}-n list element')
    if iterator < 4:
        f1.append(element - 100)
    else:
        f1.append(element + 100)
    iterator += 1

print('Was ', y)
print('Now ', f1)

#итерирование встроеным методом python
for element in enumerate(y):
    #print(type(element)) #tuple - кортеж, похож на список, нельзя изменять размер, значение и записывается в ()
    print(f'{element[1]} is {element[0]}-n list element')

t = tuple()
t = (5, 7, 12)
print(len(t))
print(sum(t))
print(t[0], ' ', t[-1])

converted_tuple = list(t)
converted_tuple[0] = 4
print(converted_tuple)

#нельзя вот так
#t[0] = 54
#t.append(55)

print(type(t))

if isinstance(t, tuple):
    t = list(t)

t[0] = 35
x = False
if isinstance(x, str):
    print(x.capitalize())
elif isinstance(x, int):
    print(x / 5)
else:
    print(x)


#ДОПИСАТЬ ОСТАТОК КОДА ИЗ СКРИНОВ И КОДА ПРЕПОДАВАТЕЛЯ