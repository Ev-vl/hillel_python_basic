from re import A


def add(a,b):
    print('finction')

    return a + b


print('not function')

add('a', 'b')

print('a', 'b', 'c', 1,2,3,4, sep='-', end='!...\n\n')


#def my_func(variable_name, input_phrase='Input number'):
    # argument = параметр функции
#    return float(input(f'>>{input_phrase} {variable_name}'))


#x = my_func(1)
#print(x)
x = '1.0'
def add_everithing(*args, z='Here is text'):
    sum = ''
    print(len(args)) #lenght
    for x in args:
        sum = sum + x
    print(z)
    return sum

#print(add_everithing(2,3,4,5, z='Here is text 1'))
print(add_everithing('a', 'b', 'c', z='Here is text 2'))

print('-----------------------------------------')
def add_menu_item():
    global menu
    new_item = input('Name of new element: ')
    new_item_price = input('New price: ')
    #menu = menu + '\n' + new_item + ' ' + new_item_price
    menu += '\n' + new_item + ' ' + new_item_price

#для чтения внешних переменных объявлять global не нужно
def display_menu():
    #вывети информацию
    print(f'Here is menu:\n{menu}')
    print("""
1. Add new elementin menu
2. Invive client
3. Exit
""")


menu = ''
while False:
    #считать выбор пользователя
    num1 = input(">> Input 1 or 2: ")
    #логика выбора
    if num1 == '1':
        add_menu_item()
    elif num1 == '2':
        pass
    elif num1 == '3':
        break

def read_triangle_values(name):
    while True:
        x = input(f'{name} = ')
        try:
            x = float(x)
            if x > 0:
                return x
        except Exception:
            print('Wrong value!')



print('-----------------------------------------')
def perimeter_triangle(a,b,c):
    return a + b + c

def square_triangle(a,b,c):
    p = perimeter_triangle(a,b,c) / 2
    square = pow(p * (p - a) * (p - b) * (p - c), 0.5)
    return square

def triangle_check(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print('Треугольник сещуствует')   
        return True
    else:
        print('Треугольник не сещуствует')
        return False


print('#' * 10)
print('Проверка треугольник')
a = read_triangle_values('a')
b = read_triangle_values('b')
c = read_triangle_values('c')

if triangle_check(a,b,c):
    print('Perimeter = ', perimeter_triangle(a,b,c))
    print('Square = ', square_triangle(a,b,c))


#PEP 8
# MyStr - CamelCase - в классах
# my_str - snake_case - переменные и функции
# MY_STR - uppercase snake_case - константы