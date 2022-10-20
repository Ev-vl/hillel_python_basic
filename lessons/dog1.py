class Dog:
    def __init__(self, name: str, age: int, breed: str):  # initialization
        self.name = name  # 'Default name'
        self.age = age  # int()
        self.breed = breed  # 'Default breed'

    def say_woof(self):
        print(f'A dog of {self.breed} breed and name {self.name} says Woof!')

    def live_one_day(self):
        if self.breed == 'corgi':
            print('Похоже, теперь вокруг много шерсти...может это ', self.name)
        elif self.breed == 'alabay':
            print('Походе, всё вокруг в чьих-то слюнях... может это ', self.name)
        else:
            print('Вам повезло :)')

    def __str__(self):
        return f'Собака по имени {self.name}, породы {self.breed}, {self.age} лет'

    def __gt__(self, other) -> bool:  # greaten then >
        if isinstance(other, Dog):
            if self.age > other.age:
                print(f'{self.name} младше, потому что ей {self.age} лет, а {other.name} - {other.age}')
                return True
            else:
                print(f'{self.name} старше, потому что ей {self.age} лет, а {other.name} - {other.age}')
                return False

if __name__=='__main__':
    random_dog = Dog(name='test', age=1, breed='test')