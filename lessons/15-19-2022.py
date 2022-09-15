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

def add_menu_item():
    global menu
    new_item = input('Name of new element: ')
    new_item_price = input('New price: ')
    #menu = menu + '\n' + new_item + ' ' + new_item_price
    menu += '\n' + new_item + ' ' + new_item_price

menu = ''
while True:
    print(f'Here is menu:\n{menu}')
    print("""
1. Add new elementin menu
2. Invive client
""")
    num1 = input(">> Input 1 or 2: ")
    if num1 == '1':
        add_menu_item()
    elif num1 == '2':
        print(num1)
