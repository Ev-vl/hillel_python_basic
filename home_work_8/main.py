# ----------- Notepad -----------#

# Логика программы:
#   Пользователю доступно на выбор 7 команд.
#   Перед вводом команды идёт проверка на наличие заметок в локальном файле JSON и в случае наличия = предлагает
#   пользователю загрузить их.
#   Пользователь вводит команду. Переменная user_command_input типа str автоматически переводится в нижний регистр для
#   стабильности.
#   Если введена некоректная команда - цикл начинается заново.
#   Первыми идут команды без обработки - help и exit.
#   В случае ввода команды add в локальный словарь user_note_data записывается соответствие дата - заметка.
#   Команды clear и load выполняются только после проверки непустых записей в файле JSON. Первая команда удаляет его
#   и очищает локальный словарь, вторая - записывает в локальный словарь user_note_data все записи из файла JSON.
#   Далее идёт проверка пустого количества заметок. Если пусто - выводится ошибка пользователю и цикл начинается заново.
#   Команда save сохраняет записи из user_note_data в файл JSON.
#   Последние четыре команды выводят отсортированный список заметок, введённых пользователем.
#   Примечание 1: я перешёл с Visual Studio на PyCharm и мне сразу выбилось много ошибок PEP, исправил это
#   Примечание 2: я починил ошибку сортировки
#   Примечание 3: Если это самый первый запуск программы - файла JSON нет, так как нет заметок. При сохранении -
#   он создастся автоматически.


import json
import os
from datetime import datetime


def add_date():
    """
        Функция возврата текущей даты в виде строки.

        return : значение типа datetime формата (%Y, %m, %d, %H, %M, %S)
    """

    datetime_now = datetime.now()
    data_param = datetime_now.year, datetime_now.month, datetime_now.day, datetime_now.hour, datetime_now.minute, \
                 datetime_now.second

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


def print_sorted_dict(dict_data: dict, reversed_mode: bool, note_mode: bool):
    """
        Функция вывода сортированного словаря. Параметры:
        --- dict_data : словарь, который нужно отсортировать.
        --- reversed_mode : булевое значение для переключения режима reverse в функции sorted().
        --- note_mode : булевое значение, True - режим сортировки по длине заметки, False - по дате.
        
        return : Null
    """

    print('Your sorted notes by date:')

    if note_mode:
        sorted_dict = sorted(dict_data.items(), reverse=reversed_mode, key=lambda x: len(x[1]))
    else:
        sorted_dict = sorted(dict_data.items(), reverse=reversed_mode, key=lambda x: x[0])

    for item, value in sorted_dict:
        print(f'Data: {item.year}.{item.month}.{item.day} 'f'{item.hour}:{item.minute}:{item.second}. '
              f'Note: {value}')


def save_notes_to_db(dict_data: dict, file_name: str):
    """
        Функция сохранения заметок в файл JSON из локального словаря. Параметры:
        --- dict_data : словарь, с которого идёт сохранение.
        --- file_name : строка с именем файла JSON

        return : Null
    """

    history = []

    for item, value in dict_data.items():
        history.append({
            'date': str(item),
            'note': value
        })

    json.dump({"history:": history}, open(file_name, mode='w'), indent=4)
    print('Saved.')


def check_notes_from_db(file_name: str):
    """
        Функция проверки заметок в файле JSON. Параметры:
        --- file_name : строка с именем файла JSON.
        
        return : если файл не пустой - True, если пустой - False.
    """

    try:
        with open(file_name) as fn:
            load_data = json.load(fn)
        return True
    except Exception:
        return False


def load_notes_from_db(file_name: str):
    """
        Функция загрузки заметок из файла JSON. Параметры:
        --- file_name : строка с именем файла JSON.
        
        return : словарь с загруженными заметками из файла JSON.
    """

    with open(file_name) as fn:
        load_data = json.load(fn)
        new_dict_data = {}
        print('Your saved notes:')
        for item in load_data["history:"]:
            date_from_item = datetime.strptime(item['date'], '(%Y, %m, %d, %H, %M, %S)')
            note_from_item = item['note']
            print(f'Data: {date_from_item.year}.{date_from_item.month}.{date_from_item.day} '
                  f'{date_from_item.hour}:{date_from_item.minute}:{date_from_item.second}. '
                  f'Note: {note_from_item}')
            new_dict_data[date_from_item] = note_from_item
        print('Loaded.')
        return new_dict_data


def clear_notes(file_name: str):
    """
        Функция удаления файла JSON. Параметры:
        --- file_name : строка с именем файла JSON.

        return : пустой словарь.
    """

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    os.remove(path)
    print('Cleared.')
    return {}


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

        # Перед вводом команды выполняется проверка на наличие заметок в JSON файле и пустом словаре и предлагает
        # пользователю загрузить их.
        if check_notes_from_db(file_name) and len(user_note_data) == 0:
            if input('You have unloaded notes. Do you want to load it? y/n\n>>> ').lower() == 'y':
                user_note_data = load_notes_from_db(file_name)

        user_command_input = input('Enter command: ').lower()

        # Проверка введённой команды пользователя.
        if not user_command_check(user_command_input):
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
            user_str = input(f'Date {date_now[0]}.{date_now[1]}.{date_now[2]} {date_now[3]}:{date_now[4]}:'
                             f'{date_now[5]}. Write note:\n>>>')
            user_note_data[date_now] = user_str

        # Блок if для команды load. Проверяется наличие заметок в JSON файле и только после этого идёт загрузка
        elif user_command_input == 'load':
            if check_notes_from_db(file_name):
                user_note_data = load_notes_from_db(file_name)
            else:
                print('No any local notes!')

        # Блок if для команды clear. Проверяется наличие заметок в JSON файле и только после этого идёт удаление
        elif user_command_input == 'clear':
            if check_notes_from_db(file_name):
                user_note_data = clear_notes(file_name)
            else:
                print('No any local notes!')

        # Блок if для проверки нулевого количества заметок, если есть заметки - выполняется одна из команд сортировки.
        elif len(user_note_data) == 0:
            print('No any notes!')
            continue

        # Блок if для команды save.
        elif user_command_input == 'save':
            save_notes_to_db(user_note_data, file_name)

        # Блок if для команд сортировки.
        elif user_command_input == 'earliest':
            print_sorted_dict(user_note_data, False, False)

        elif user_command_input == 'latest':
            print_sorted_dict(user_note_data, True, False)

        elif user_command_input == 'longest':
            print_sorted_dict(user_note_data, True, True)

        elif user_command_input == 'shortest':
            print_sorted_dict(user_note_data, False, True)
