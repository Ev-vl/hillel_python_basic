from dog1 import Dog


bob = Dog(name='Bob', age=4, breed='shepherd dog')

print(bob)
print(type(bob))

print(bob.name, type(bob.name))
print(bob.age, type(bob.age))

light = Dog(name='Light', age=6, breed='corgi')
print(light)
print(light.name, type(bob.name))
print(light.age, type(bob.age))

nick = Dog(name='Nick', age=3, breed='alabay')  # если переменная не используется в расчётах, то
# можно испозовать любой тип данных
print(nick)

print('#' * 15)
bob.say_woof()
light.say_woof()
nick.say_woof()

print('#' * 15)
bob.live_one_day()
light.live_one_day()
nick.live_one_day()

print('#' * 15)
nick > light
bob > light
nick > bob

print('#' * 15)
nick < light
bob < light
nick < bob
