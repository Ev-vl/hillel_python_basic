import os.path
from random import choice
import json


class ChatBot:
    def __init__(self, name, vocalub: dict):
        self.name = name
        self.vocab = vocalub

    def save(self):
        file_name = f'{self.name}.json'
        json.dump(self.vocab, open(file_name, 'w'), indent=4)
        print(f'Bot saved in file {file_name}')

    def load(self):
        file_name = f'{self.name}.json'
        if os.path.isfile(file_name):
            self.vocab = json.load(open(file_name))
            print(f'Bot loaded from file {file_name}')
        else:
            print(f'I can find any file {file_name}')

    def have_a_conversation(self):
        while True:
            user_input = self.get_from_user('You: ')
            exit_flag = self.respond(message=user_input.lower())

            if exit_flag:
                break

    def print_respond(self, response: str):
        print(f'{self.name}: {response}')

    def get_from_user(self, message: str):
        user_input = input('You: ')
        return user_input

    def learn_from_user(self, message: str):

        new_word = choice(message.split())

        self.print_respond(f'What do you mean about {new_word}')
        user_input = self.get_from_user('You: ')
        self.vocab[new_word] = ([user_input], False)

    def respond(self, message: str):
        for key, (response_options, exit_flag) in self.vocab.items():
            if key in message:
                self.print_respond(choice(response_options))
                return exit_flag

        self.learn_from_user(message)
        return False


if __name__ == '__main__':
    chatbot = ChatBot(name='Neil', vocalub={
        "hello": (['Hello!', 'Hello, I\'m bot!'], False),
        "good morning": (['Good morning!', 'Good morning, I\'m bot!'], False),
        "hi": (['Hi!', 'Hi, I\'m bot!'], False),
        "good night": (['Good night!', 'Good night, I\'m bot!'], False),
        "bye": (['Bye!', 'See you!'], True)
    })
    chatbot.load()
    chatbot.have_a_conversation()
    chatbot.save()
