#----------- Сума введених чисел -----------#

#number check
def return_user_input():
    user_input = input(f'Enter number, \'sum\' or \'exit\': ')
    while True:
            
            if user_input == 'sum' or user_input == 'exit':
                return user_input

            try:
                user_input = float(user_input)
                return user_input
            except Exception: 
                user_input = input(f'Wrong value! Enter number or sum: ')
            

if __name__ == '__main__':

    user_list = list()

    while True:
        user_input = return_user_input()
        if user_input == 'sum' and len(user_list) > 0:
            print('Sum: ', sum(user_list))
            user_list.clear()
        elif user_input == 'sum' and len(user_list) == 0:
            print('Empty error!')
        elif user_input == 'exit':
            print('Goodbye!')
            break
        else:
            user_list.append(user_input)

