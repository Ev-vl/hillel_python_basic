# ----------- Notepad -----------#

# Логика программы:
#   Пользователю доступно на выбор 7 команд.
#   Пользователь вводит команду. Переменная user_command_input типа str автоматически переводится в нижний регистр для стабильности.
#   Если введена некоректная команда - цикл начинается заново.
#   Первыми идут команды без обработки - help и exit.
#   Далее идёт проверка пустого количества заметок. Если пусто - выводится ошибка пользователю и цикл начинается заново.
#   Последние четыре команды выводят отсортированный список заметок, введённых пользователем.
#   Примечание: я использовал тип datetime для корректной сортировки по дате
#   Примечание 2: я починил ошибку сортировки


#На чём остановился - добавить проверку на пустую базу данных для записи (дополнительно можно добавить проверку
# на пустую переменную user_note_data для выведения разных комментариев), добавить функцию для удаления заметок и


import json
import os
import time
from datetime import datetime


def add_date():
    """
        Функция возврата текущей даты в виде строки.

        return : значение типа datetime
    """

    date_now = datetime.now()
    data_param = date_now.date(), date_now.hour, date_now.minute, date_now.second

    return data_param


def user_command_check(u_s_i: str):
    """
        Функция проверки введенной команды пользователя. Параметр:
        --- u_s_i : сокращенное от user_command_input, введённое значение пользователя.

        return : верна ли команда (true/false)
    """

    commands_list = [
        'add',
        'save',
        'load',
        'clear',
        'earliest',
        'latest',
        'longest',
        'shortest',
        'help',
        'exit'
    ]

    for i in commands_list:
        if u_s_i == i:
            return True

    return False


def print_sorted_dict(dict_data: dict, reversed_mode: bool, key: int, note_mode: bool):
    """
        Функция вывода сортированного словаря. Параметры:
        --- dict_data : словарь, который нужно отсортировать.
        --- reversed_mode : булевое значение для переключения режима reverse в функции sorted().
        --- key : вводит значения 0 или 1 для сортировки по ключу или значению словаря, соответственно.
        
        return : Null
    """

    print('Your sorted notes by date:')

    if note_mode:
        sorted_dict = sorted(dict_data.items(), reverse=reversed_mode, key=lambda x: len(x[1]))
    else:
        sorted_dict = sorted(dict_data.items(), reverse=reversed_mode, key=lambda x: x[key])

    for item, value in sorted_dict:
        print(f'Data: {item[0]} {item[1]}:{item[2]}:{item[3]}. Note: {value}')


def save_notes_to_db(dict_data: dict, file_name: str):
    history = []

    for item, value in dict_data.items():
        history.append({
            'date': str(item),
            'note': value
        })

    json.dump({"history:": history}, open(file_name, mode='w'), indent=4)


def load_notes_to_db(file_name):
    with open(file_name) as fn:
        load_data = json.load(fn)
        new_dict_data = {}
        print('Your saved notes:')
        for item in load_data["history:"]:
            date_from_item = datetime.strptime(item['date'], '(datetime.date(%Y, %m, %d), %H, %M, %S)')
            note_from_item = item['note']
            print(f'Data: {date_from_item.year}.{date_from_item.month}.{date_from_item.day} '
                  f'{date_from_item.hour}:{date_from_item.minute}:{date_from_item.second}. '
                  f'Note: {note_from_item}')
            new_dict_data[date_from_item] = note_from_item
        print('Loaded.')
        return new_dict_data


if __name__ == '__main__':

    user_note_data = dict()
    file_name = 'user_db.json'

    print("""Hello! It's notepad programm. Commands list:
    --- add : add new note
    --- save : save all notes
    --- load : load all notes
    --- clear : clear all notes
    --- earliest : display the saved notes in chronological order - from the earliest to the latest;
    --- latest : display saved notes in chronological order - from the latest to the earliest;
    --- longest : displays the saved notes in the order of their length - from the longest to the shortest;
    --- shortest : displays the saved notes in the order of their length - from shortest to longest;
    --- help : display commands list.
    --- exit: exit from programm
    """)

    while True:

        user_command_input = input('Enter command: ').lower()

        # Проверка введённой команды пользователя.
        if user_command_check(user_command_input) == False:
            print('Wrong command! Try again.')
            continue

        # Блок if - elif для вывода команд help/exit.
        elif user_command_input == 'help':
            print("""Commands list:
    --- add : add new note
    --- save : save all notes
    --- load : load all notes
    --- clear : clear all notes
    --- earliest : display the saved notes in chronological order - from the earliest to the latest;
    --- latest : display saved notes in chronological order - from the latest to the earliest;
    --- longest : displays the saved notes in the order of their length - from the longest to the shortest;
    --- shortest : displays the saved notes in the order of their length - from shortest to longest;
    --- help : display commands list.
    --- exit: exit from programm
    """)
        elif user_command_input == 'exit':
            print('Goodbye!')
            break

        # Блок if для вывода команды add.
        elif user_command_input == 'add':
            date_now = add_date()
            user_str = input(f'Date {date_now[0]} {date_now[1]}:{date_now[2]}:{date_now[3]}. Write note:\n>>>')
            user_note_data[date_now] = user_str

        elif user_command_input == 'load':
            user_note_data = load_notes_to_db(file_name)

        # Блок if для проверки нулевого количества заметок, если есть заметки - выполняется одна из команд сортировки.
        elif len(user_note_data) == 0:
            print('No any notes!')
            continue

        elif user_command_input == 'save':
            save_notes_to_db(user_note_data, file_name)

        elif user_command_input == 'earliest':
            print_sorted_dict(user_note_data, False, 0, False)

        elif user_command_input == 'latest':
            print_sorted_dict(user_note_data, True, 0, False)

        elif user_command_input == 'longest':
            print_sorted_dict(user_note_data, True, 1, True)

        elif user_command_input == 'shortest':
            print_sorted_dict(user_note_data, False, 1, True)