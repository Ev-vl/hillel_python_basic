#----------- Bot from Ukraine :) -----------#

user_input = input('Let\'s start to talk with bot. Input text: ')

while True:
    if user_input.__contains__('Hello') or  user_input.__contains__('Hi') or  user_input.__contains__('Good morning') or  user_input.__contains__('Good evening'):
        print('Bot: Hello! I\'m bot from Ukraine.')
        user_input = input('You: ')

    elif user_input.__contains__('How are you') or  user_input.__contains__('What are you doing'):
        print('Bot: I\'m learning Python.')
        user_input = input('You: ')

    elif user_input.__contains__('Film') or  user_input.__contains__('Serial') or  user_input.__contains__('Cinema') or user_input.__contains__('film') or user_input.__contains__('serial') or user_input.__contains__('cinema'):
        print('Bot: Sorry for interrupting, I don\'t know what you mean, but I want to recommend the film that called \'The Shawshank Redemption\', it is good!')
        user_input = input('You: ')

    elif user_input.__contains__('Bye') or  user_input.__contains__('Good night') or  user_input.__contains__('Goodbye'):
        print('Bot: See you!')
        break
    
    else:
        print('Bot: Sorry, but I don\'t understand you. Please write again.')
        user_input = input('You: ')
    