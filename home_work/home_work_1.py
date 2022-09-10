#-----Converte degrees to radians-----

import math


#checking is it number
degree = input("Enter degree: ")
while type(degree) != int or type(degree) != float:
        
        try:
            degree = float(degree)
            break
        except Exception: 
            degree = input('It is not a number! Enter dergee: ')


#transform degree to radian
radian = (degree * math.pi)/180
print(f'Radian of {degree} = {round(radian, 4)}')