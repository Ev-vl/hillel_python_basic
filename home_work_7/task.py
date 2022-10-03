#----------- Notepad -----------#

#Логика программы:
#   Пользователю доступно на выбор 7 команд.
#   Пользователь вводит команду. Переменная user_command_input типа str автоматически переводится в нижний регистр для стабильности.
#   Если введена некоректная команда - цикл начинается заново.
#   Первыми идут команды без обработки - help и exit.
#   Далее идёт проверка пустого количества заметок. Если пусто - выводится ошибка пользователю и цикл начинается заново.
#   Последние четыре команды выводят отсортированный список заметок, введённых пользователем.
#   Примечание: я использовал тип datetime для корректной сортировки по дате



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


    if u_s_i == 'add' or u_s_i == 'earliest' or u_s_i == 'latest' or u_s_i == 'longest' or u_s_i == 'shortest' or u_s_i == 'help' or u_s_i == 'exit':
        return True
    else:
        return False

def print_sorted_dict(dict_data: dict, reversed_mode: bool, key: int):
       
    """
        Функция вывода сортированного словаря. Параметры:
        --- dict_data : словарь, который нужно отсортировать.
        --- reversed_mode : булевое значение для переключения режима reverse в функции sorted().
        --- key : вводит значения 0 или 1 для сортировки по ключу или значению словаря, соответственно.
        
        return : Null
    """

    print('Your sorted notes by date:')

    sorted_dict = sorted(dict_data.items(), reverse = reversed_mode, key = lambda x:x[key])

    for item, value in sorted_dict:
        print(f'Data: {item[0]} {item[1]}:{item[2]}:{item[3]}. Note: {value}')




if __name__ == '__main__':

    
    user_note_data = dict()

    print("""Hello! It's notepad programm. Commands list:
    --- add : add new note
    --- earliest : display the saved notes in chronological order - from the earliest to the latest;
    --- latest : display saved notes in chronological order - from the latest to the earliest;
    --- longest : displays the saved notes in the order of their length - from the longest to the shortest;
    --- shortest : displays the saved notes in the order of their length - from shortest to longest;
    --- help : display commands list.
    --- exit: exit from programm
    """)
    
    while True:

        user_command_input = input('Enter command: ').lower()

        #Проверка введённой команды пользователя.
        if user_command_check(user_command_input) == False:
            print('Wrong command! Try again.')
            continue

        #Блок if - elif для вывода команд help/exit.
        elif user_command_input == 'help':
            print("""Commands list:
    --- add : add new note
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

        #Блок if для вывода команды add.
        elif user_command_input == 'add':
            date_now = add_date()
            user_str = input(f'Date {date_now[0]} {date_now[1]}:{date_now[2]}:{date_now[3]}. Write note:\n>>>')
            user_note_data[date_now] = user_str

        #Блок if для проверки нулевого количества заметок, если есть заметки - выполняется одна из команд сортировки.
        elif len(user_note_data) == 0:
            print('No any notes!')
            continue

        elif user_command_input == 'earliest':
            print_sorted_dict(user_note_data, False, 0)

        elif user_command_input == 'latest':
            print_sorted_dict(user_note_data, True, 0)
        
        elif user_command_input == 'longest':
            print_sorted_dict(user_note_data, True, 1)
        
        elif user_command_input == 'shortest':
            print_sorted_dict(user_note_data, False, 1)
        
            
        
