
def old_code():
    x = [3,4,5]
    #compregended_powered_x = [element ** 2 for element in x]
    #одно и то же
    #regular_powered_x = list()
    #for element in x:
    #    regular_powered_x.append(element ** 2)


    #new_list = [element for element in range(5,100,3)]

    ##list(range(5,100,3))

    ##[*результат* for *называем имя итерируемого* in *то откуда берём элементы* ]


    #x = [3,5,7,100,150,600]
    #compregended_filtered_x = [element for element in x if element < 100]
    ##одно и то же
    #regular_powered_x = list()
    #for element in x:
    #    regular_powered_x.append(element)

    #print(compregended_filtered_x)
    #print(regular_powered_x)
    print()





#для чтения внешних переменных объявлять global не нужно
def display_menu(menu: list):
    #вывети  информацию
    print('Меню:')
    for i, item in enumerate(menu):
        print(f' {i+1}. {item[0]} - {item[1]} UAH')

def read_menu_item(menu: list) -> tuple:

    user_input = input("Что вы желаете? >>  ")

    try:
        user_input = int(user_input)
    except Exception:
        print('Введите, пожалуйста, пункт меню (цифрой).')
        return tuple()
    
    if 0 < user_input <= len(menu):
        return menu[user_input - 1]

    print('Введите, пожалуйста, пункт меню (цифрой).')
    return tuple()

def is_client_ordering() -> int:

    print('1. Заказать\n2.Выйти')

    user_input = input("Ваш выбор: ")

    try:
        user_input = int(user_input)
    except Exception:
        print('Введите, пожалуйста, пункт меню (цифрой).')
        return -1

    if user_input == 1:
        return 1
    elif user_input == 2:
        return 2
    else:
        print('Ошибка ввода. Введите, пожалуйста, пункт меню (цифрой).')
        return -1



if __name__ != '__main__': #код с рестораном
    restourant_menu = [
        ('Кофе', 18),
        ('Чай', 15),
        ('Какао', 12),
        ('Булочка с вышней', 10)
    ]

    client_balance = 100

    while True:
        print('-----------------------------------------')
        is_ordering = is_client_ordering()
        if is_ordering == 1:
            display_menu(restourant_menu)
            print(f'У вас на счету {client_balance} UAH')

            chosen_item = read_menu_item(restourant_menu)
            if chosen_item:
                if client_balance > chosen_item[1]:
                    client_balance -= chosen_item[1]
                    print(f'Вот ваш заказ: {chosen_item[0]}, с вашего счёта снято {chosen_item[1]} UAH. Баланс: {client_balance} UAH. Баланс: {client_balance} UAH.') 
                else:
                    print(f'Недостаточно средств на счету. Баланс {client_balance}.')
            else:
                pass
        elif is_ordering == 2:
            exit(0)


if __name__ == '__main__':
    #dictionary

    d = {
        "я":"I",
        "Моё":"my",
        "Питон":"Python",
        "учусь":"learn",
        "программировать":'to program',
        "на":"on"
    }

    print(d['Питон'])

    d = {
        0: 3,
        1: 4,
        2: 5
    }

    print(d[0], d[1], d[2])

    d = {
        'name':'Coffee',
        'price':18
    }

    #добавление значения
    d['desription'] = 'none'

    print(d['desription'])

    #keys/values
    print(d.keys())
    print(d.values())

    #выбор чего-то отдельно
    for item in d.values(): #можно выбирать просто d (тоже самое, что и d.keys()), можно выбрать values()
        print(item)

    #выбор и того, и того через items()
    print(d.items(), list(d.items()))
    for item, value in d.items():
        print(item,  value)
    #одно и то же, разный метод
    for item in d.items():
        print(item, item[0], item[1])
    