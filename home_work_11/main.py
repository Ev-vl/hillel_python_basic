# --------- Online store --------- #
# Theme: kitchen items and dishes


import json
import items


def return_float(str_print: str):
    """
        Функция, которая возвращает число float. Для данного проекта не должно быть минусовое значение.Функция не
        вернёт число до тех пор, пока не будет введено верное значение Параметры:
        --- str_print : строка, которая выводится для ввода числа

        return : положительное число float
    """

    num = input(str_print)
    while type(num) != int or type(num) != float:

        try:
            num = float(num)
            if num >= 0:
                return num
            else:
                num = input(f'Wrong value! Enter number: ')
        except Exception:
            num = input(f'Wrong value! Enter number: ')


def value_check(print_str: str, input_list: list):
    """
        Функция, которая проверяет наличия строки в списке данных. В ней все строки приводятся к нижнему регистру чтобы
        минимизоровать ошибки и сделать её универсальной. Функция не вернёт строку до тех пор, пока не будет введено
        верное значение. Параметры:
        --- print_str : строка, которую нужно проверить
        --- input_list : списке, в котором проверяется наличие значения переменной

        return : верное значение из списка данных
    """

    check_value = input(print_str).lower()

    while True:
        for a in input_list:
            if a.lower() == check_value:
                return check_value
        check_value = input("Wrong value! Enter again, please: ").lower()


def return_item(category_input: str, categories: list, data: dict):
    """
        Функция возврата объект дочернего класса в зависимости от выбранной категории. Параметры:
        --- category_input : введённая пользователем категория
        --- categories : список категорий, тип данных - class
        --- data : данные одного товара

        return : обект класса выбранной категории
    """

    for category_class in categories:
        if category_input == category_class.__name__:
            return category_class(name=data['name'], price=data['price'], quantity=data['quantity'],
                                  additional_data=data['additional_data'])


def print_items_by_filter(category_input: str, main_data: dict, categories: list):
    """
        Функция вывода товаров в зависимости от выбранного фильтра. Этапы:
        1. Выводятся возможные фильтра товара в выбранной категории.
        2. Выбирается фильтр. Программа не продолжится до тех пор, пока не будет введена правильный фильтр.
        3. Если тип значений выбранного фильтра число - нужно ввести интервал из 2 чисел. После этого  выводятся товары
           из выбранного диапазона и категории.
           Если же строка - нужно ввести строковое значение для этого фильтра. Проверка на значение не выполняется,
           поэтому выводятся товары, если находится совпадение.
        4. Выводится к-во найденных товаров и предложения выйти из режима фильтрации.
        Параметры:
        --- category_input : введённая пользователем категория
        --- categories : список категорий, тип данных - class
        --- main_data : база данных всех товаров

        return : решение пользователя выйти из режима фильтрации.
    """

    print("You can choose next filter:")
    Item = {}
    for md in main_data:
        if category_input == md['category']:
            Item = return_item(category_input, categories, md)
            break

    filters_dict = Item.return_filter_print()

    for fl in filters_dict.keys():
        print(fl)

    filter_input = input("Choose one: ").lower().title()
    stop_value = False
    filter_type = ""

    while not stop_value:
        for item, value in filters_dict.items():
            if item == filter_input:
                stop_value = True
                filter_type = value
                break
        if not stop_value:
            filter_input = input("Wrong filter! Enter again, please: ").lower()

    if filter_type == type(int()) or filter_type == type(float()):
        between_1 = return_float("For this filter must be interval. Please, enter"
                                 " first number: ")
        between_2 = return_float("Enter second number: ")

        for data in main_data:
            if data['category'] == category_input and between_1 <= data['price'] <= between_2:
                print(return_item(category_input, categories, data))

    elif filter_type == type(str()):

        user_filter_input = input("For this filter enter, please, your value: ").lower()
        count_elements = 0

        for data in main_data:
            if data['category'] == category_input:

                for item, value in data.items():
                    try:
                        if filter_input.lower() == item and user_filter_input == value:
                            print(return_item(category_input, categories, data))
                            count_elements += 1
                    except Exception:
                        pass

                if data['additional_data'].items() != {}:
                    for item, value in data['additional_data'].items():
                        try:
                            if filter_input.lower() == item and user_filter_input == value:
                                print(return_item(category_input, categories, data))
                        except Exception:
                            pass

    exit_mode = input(f"Founded {count_elements} items. Do you exit (y/n): ")
    if exit_mode == 'y':
        print("Exit.")
        return True
    else:
        return False


if __name__ == "__main__":

    file_name = "warehouse.json"

    commands_list = [
        "category",
        "filter",
        "reset",
        "exit"
    ]

    categories = [
        items.Pan,
        items.Pot,
        items.Knife,
        items.Plate,
        items.Cup
    ]

    categories_name = [
        items.Pan.__name__,
        items.Pot.__name__,
        items.Knife.__name__,
        items.Plate.__name__,
        items.Cup.__name__
    ]

    print("Hello! First-look shop welcomes you!")

    with open(file_name) as csvfile:

        # Загрузка данных из файла JSON. Весь функционал программы записал внутрь with open() чтобы не дублировать
        # загрузку файла
        main_data = json.load(csvfile)

        reset_mode = True
        exit_mode = False

        while True:
            # Блок первоначального экрана и возможностью завершить программу
            if reset_mode:

                print("Categories to search in:")
                for i in categories:
                    print("  " + i.__name__)
                category_input = value_check("Choose category name or 'exit': ", input_list=categories_name).title()
                if category_input.lower() == 'exit':
                    print("Goodbye!")
                    break
                reset_mode = False

            # Блок вывода товаров в категории, выбора фильтра или возможностью выйти в начальный экран
            elif not reset_mode:

                print(f"Items in {category_input} category:\n")
                count = 0
                # Вывод товаров в соответствии с категорией
                for i in main_data:
                    if category_input == i['category']:
                        print(return_item(category_input=category_input, categories=categories, data=i))
                        count += 1
                # Выбор фильтра
                filter_mode = value_check(
                    f"Found {count} {category_input.lower()}(s). Would you like to set filter or " +
                    "reset: ", input_list=commands_list)

                # Блок фильтрации будет происходить до тех пор, пока не будет выбран параметр выхода из него
                if filter_mode.lower() == 'filter':
                    while not exit_mode:
                        exit_mode = print_items_by_filter(category_input, main_data, categories)

                # Блок возврата в первоначальный экран
                elif filter_mode.lower() == 'reset':
                    reset_mode = True
