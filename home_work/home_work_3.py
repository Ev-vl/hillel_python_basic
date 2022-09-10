#Delete symbols '.,;:!?'

str1 = input('Input string: ')

str1 = str1.replace('.', '')
str1 = str1.replace(',', '')
str1 = str1.replace(';', '')
str1 = str1.replace(':', '')
str1 = str1.replace('!', '')
str1 = str1.replace('?', '')


print('New string: ', str1)