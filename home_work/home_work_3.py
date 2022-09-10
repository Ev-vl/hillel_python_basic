#-----Delete symbols '.,;:!?'-----

str1 = input('Input string: ')


#remove symbols to empty
str1 = str1.replace('.', '')
str1 = str1.replace(',', '')
str1 = str1.replace(';', '')
str1 = str1.replace(':', '')
str1 = str1.replace('!', '')
str1 = str1.replace('?', '')


print('New string: ', str1)